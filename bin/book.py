from os import system, listdir, environ, chdir
from os.path import join, isfile, exists
from sys import argv

from tst import shell
from book_test import book_checker


def book_build():
    '''Put together a markdown file from the individual parts '''
    results = 'Build: Book.md\n'
    chapters = ['chapters/'+i for i in book_read_index('Chapters')]
    with open('Book.md','w') as output_file:
        for p in chapters:
            path = p+'.md'
            results += 'Build '+path+'  ...\n'
            text = open(path).read()    
            output_file.write(text+'\n\n\\newpage\n---\n\n')
    print(results)


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
        system('e '+join(environ['book'],argv[2]))
    else:
        system('e '+environ['book'])


def book_headlines():
    for i in book_read_index('Chapters'):
        path = join(environ['book'],'chapters',i+'.md')
        headline = open(path).read().split('\n')[0]
        print('%-15s ' % i + headline)


def book_index():
    def print_index_entry(category, path, title):
        print('- [%s.md, "%s", "%s"]' % (category+'/'+path, category, title))

    print('site_name: Software Leverage\n\npages:\n')
    for i in book_read_index('Chapters'):
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
*     dired                 -- Edit the book content directory
*     edit                  -- Edit the book content
*     files                 -- List all of the files
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
        'Cover;Abstract;Contents;Overview;Summary',
        'Intro;Leverage;Debt;Practices',
        'Technology;Design;Code;Test',
        'Services;Release;Scaling;Monitoring',
        'Knowledge;Teamwork;Learning;Planning'
    ]
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


def book_text(chapter=1):
    '''Display the raw text of one chapter'''
    f = join(environ['book'], 'chapters', '%s.md'%chapter)
    print(open(f).read())


def book_calculate_words(label,files):
    '''Measure the words for a file set'''
    print(label)
    text = [shell('wc -w '+topic) for topic in files if exists(topic)]
    print(''.join(text))


def book_words():
    '''Count all of the words in the book '''
    book = ['book/'+i+'.md' for i in book_read_index('Book')] 
    chapters = ['chapters/'+i+'.md' for i in book_read_index('Chapters')]
    content  = ['content/'+i+'.outline'  for i in book_read_index('Chapters')]
    chdir(environ['book'])
    book_calculate_words('manuscript',['Book.md'] )
    book_calculate_words('chapters',chapters)
    book_calculate_words('content',content)
    print('\n')


def book_command(argv):
    '''Execute all of the book specific commands '''
    if len(argv)>1:
        chdir(environ['book'])
        #print(shell('ls -l'))

        if argv[1]=='build':
            print(book_build())

        elif argv[1]=='changes':
            print(book_changes())

        elif argv[1]=='commit':
            book_commit(argv)

        elif argv[1]=='dired':
            book_dired()

        elif argv[1]=='edit':
            book_edit(argv)

        elif argv[1]=='index':
            book_index()

        elif argv[1]=='headlines':
            book_headlines()

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