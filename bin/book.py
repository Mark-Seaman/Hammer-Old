from glob import glob
from os import system, listdir, environ, chdir
from os.path import join, isfile, exists
from re import sub,compile,DOTALL,IGNORECASE
from sys import argv

from tst import shell
from book_test import book_checker


def to_markdown(text):
    '''Convert ascidoc text to markdown'''
    mdtext = []
    for line in text.split('\n'):
        if line.startswith("="):
            line = line[1:].replace('=', '#').replace('Practice =', 'Practice #')
            mdtext.append(line)
        else:
            mdtext.append(line)
    return '\n'.join(mdtext)


def asc_to_markdown():
    '''Convert the book file to asciidoc'''
    with open('Book.asc') as f:
        open('Book.md','w').write(to_markdown(f.read()))


def book_build():
    '''Put together a markdown file from the individual parts '''
    results = 'Build: Book.md\n'
    chapters = ['chapters/'+i for i in book_read_index()]
    with open('Book.asc','w') as output_file:
        for p in chapters:
            path = p+'.asc'
            results += 'Build '+path+'  ...\n'
            text = open(path).read()    
            output_file.write(text+'\n\n\\newpage\n![](images/water-strip.png)\n\n')
    asc_to_markdown()
    return results


def book_changes():
    return 'Changes to Book content' + shell('git diff')


def book_commit(argv):
    '''Form the shell script for the commit command. '''
    comment = book_commit_comment(argv)
    command = '''echo Commit all changes from the book project
        git stash save &&
        git add -A . &&
        git commit -m"%s" &&
        git pull &&
        git push &&
        git stash apply
    ''' % comment
    system(command)


def book_commit_comment(argv):
    '''Select the comment to tag onto the commit. '''
    if len(argv)>2:
        return ' '.join(argv[2:])
    return 'Automatic book commit'
    

def book_convert(path=None):
    if not path:
        for path in glob('chapters/*.md'):
            book_convert(path)
    else:
        print ('convert to ASC: '+path)
        text = open(path).read().replace('#', '=').split('\n')
        with open(path.replace('.md','.asc'),'w') as f:
            for line in text:
                if line.startswith("="):
                    line = '='+line 
                f.write(line+'\n')


def book_dired():
    '''Use directory editor in emacs to edit the book content'''
    system('em $book')


def book_edit(argv):
    '''Edit the book content'''
    if len(argv)>2 and argv[2]=='index':
        yml = join(environ['book'],'../mkdocs.yml')
        system('book index > '+yml)
        system('e '+yml)
    elif len(argv)>2:
        system('e '+join(environ['book'], 'chapters', argv[2]+'.asc'))
    else:
        system('e '+environ['book'])


def book_find(words):
    if not words:
        print ('No string to search for')
        return
    chdir(join(environ['book'],'chapters'))
    system('grep -n %s %s' % (words[0],'*.asc'))


def book_headings(topic=None):
    '''Extract all of the functions from the source and count their length'''

    def find_headings(text, pattern='='):
        lines = text.split('\n')
        start = 0
        title = ''
        for i,line in enumerate(lines):
            if line.strip().startswith(pattern) or line=='****':
                pat = compile(r"\=* (.*)")
                name = pat.sub(r'\1',line)
                if '====' != name:
                    if title:
                        yield ((i-start,title))
                    start = i
                    if '****' in line:
                        title = '--'
                    else:
                        title = line.replace('=','    ')[9:]
        yield((i-start,title))

    def print_headings(topic):
        path = join(environ['book'],'chapters',topic+'.asc')
        print('\n'+topic)
        text = open(path).read()
        print('\n    major: ')
        for heading in find_headings(text, '=== '):
            print('    %3d : %-15s ' % heading)
        print('\n    minor:')
        for heading in find_headings(text):
            print('    %3d : %-15s ' % heading)

    if topic:
        print_headings(topic[0])
    else:
        for topic in book_read_index():
            print_headings(topic)


def book_headlines():
    for i in book_read_index():
        path = join(environ['book'],'chapters',i+'.asc')
        headline = open(path).read().split('\n')[0]
        print('%-15s ' % i + headline.replace('==',''))


def book_index():
    def print_index_entry(category, path, title):
        print('- [%s.md, "%s", "%s"]' % (category+'/'+path, category, title))

    print('site_name: Software Leverage\n\npages:\n')
    for i in book_read_index():
        print_index_entry('chapters', i, i) 


def book_help():
    '''Show all the book commands and their usage. '''
    print('''
*    usage: book command [args]
* 
*   commands:
*
*     build                 -- Build the content of the book
*     changes               -- List doc changes 
*     commit [message args] -- Commit all changes to the book
*     convert               -- Convert all Markdown files to Asciidoc
*     dired                 -- Edit the book content directory
*     edit                  -- Edit the book content
*     find pattern          -- Find the string in the book
*     files                 -- List all of the files
*     headlines             -- List all chapter headlines
*     headings              -- List length of all headings
*     help                  -- Show the available commands
*     list                  -- List the parts of the book
*     outline               -- Show the outline for the book
*     push                  -- Push the book to the dropbox
*     test                  -- Run all system tests
*     words                 -- Count the words
            ''')


def nested_list(name, children):
    '''Build a string that is a formatted list'''
    return '\n'+name+':    \n    '+'\n    '.join(sorted(children))


def book_list():
    '''List the parts of the book source code. '''
    results = "List the contents of this book\n"
    for d in ['.', 'chapters']:
        book_dir = join(environ['book'],d)
        files = [f for f in listdir(book_dir) if isfile(join(book_dir,f))]
        results += '\n\n'+d+':    \n    '+'\n    '.join(sorted(files))
    return results


def book_outline(topic):
    '''Build a new outline from the book text'''
    from outline import extract_headings, convert_to_outline
    f = join(environ['book'], 'chapters', '%s.md'%topic)
    headings = extract_headings(open(f).read())
    print(convert_to_outline(headings))
   

def book_pdf():
    '''Build the PDF file from the Book markdown file. '''
    system('''
        rm ../*.pdf
        pandoc Book.md    -o ../Book.pdf    2> /dev/null
        rm Book.md
        ls -s ../Book.pdf
        echo Read file with:
        echo '     pdf $book/../Book.pdf'
         ''')


def book_read():
    '''Read the PDF for the book'''
    book_pdf()
    system('pdf $book/../Book.pdf')


def book_read_index(part=None):
    '''Read an index from the book directory'''
    topics = [
        'Cover',
        'Leverage;Debt;Practices',
        'Technology;Design;Code;Test',
        'Release;Services;Deployment;Monitoring',
        'Knowledge;Teamwork;Learning;Planning'
    ]
    if part:
        topics = topics[part]
    else:
        topics = ';'.join(topics)
    
    topics = [t for t in topics.split(';') if t]
    return topics


def book_show():
    '''Run page server and point the browser to the book.'''
    print("Show the book content in a browswer")

    system('cd ..; rbg mkdocs serve; sleep 3')
    system('web http://127.0.0.1:8000/book/Cover/')


def book_status():
    '''Form the shell script for the commit command. '''
    return 'List all pending changes to the book\n' +shell('git status')


def book_text(chapter='Leverage'):
    '''Display the raw text of one chapter'''
    f = join(environ['book'], 'chapters', '%s.asc'%chapter)
    print(open(f).read())


def chapter_words(chapter):
    if exists(chapter):
        text = shell('wc -w '+chapter) 
        count = [t for t in text.split(' ') if t ]
        return int(count[0])


def book_calculate_words(label,files):
    '''Measure the words for a file set'''
    print(label)
    total = 0
    for topic in files:
        if exists(topic):
            count = chapter_words(topic) / 250
            total  += count
            topic = topic.replace('chapters/','').replace('.asc','')
            print('    %4d pages  %-30s' % (count,topic))
    if topic != 'Book':
        print('\n    %4d pages total' % total)
        print('    %4d hours to draft\n' % (total*1.5))


def book_word_count(part):
    chapters = ['chapters/'+i+'.asc' for i in book_read_index(part+1)]
    book_calculate_words('Part %d' % (part+1), chapters)


def book_words():
    '''Count all of the words in the book '''
    chdir(environ['book'])
    book_calculate_words('manuscript',['Book.md'] )
    print('\n')
    for part in range(4):
        book_word_count(part)


def book_command(argv):
    '''Execute all of the book specific commands '''
    if len(argv)>1:
        chdir(environ['book'])

        if argv[1]=='build':
            print(book_build())

        elif argv[1]=='changes':
            print(book_changes())

        elif argv[1]=='commit':
            book_commit(argv)

        elif argv[1]=='convert':
            book_convert()

        elif argv[1]=='dired':
            book_dired()

        elif argv[1]=='edit':
            book_edit(argv)

        elif argv[1]=='find':
            book_find(argv[2:])

        elif argv[1]=='index':
            book_index()

        elif argv[1]=='headlines':
            book_headlines()

        elif argv[1]=='headings':
            book_headings(argv[2:3])

        elif argv[1]=='list':
            print(book_list())

        elif len(argv)>2 and argv[1]=='outline':
            book_outline(argv[2])

        elif argv[1]=='read':
            book_read()

        elif argv[1]=='show':
            book_show()

        elif argv[1]=='status':
            print(book_status())

        elif argv[1]=='test':
            book_checker()

        elif argv[1]=='text':
            if len(argv)>2:
                book_text(chapter=argv[2])
            else:
                book_text()

        elif argv[1]=='words':
            book_words()
        
        else:
            print('No book command found, '+argv[1])
            book_help()
    else:   
        book_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    book_command(argv)