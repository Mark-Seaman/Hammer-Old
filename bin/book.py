from os import system, listdir, environ, chdir
from os.path import join, isfile
from sys import argv

from tst import shell
from book_test import book_checker

def book_assemble():
	'''
	Put together a markdown file from the individual parts
	'''
	results = 'Assemble: Index.md\n'
	parts = ['book/'+i for i in book_read_index('Book')] + ['chapters/'+i for i in book_read_index('Chapters')]
	#print('PARTS:', parts)

	with open('Book.md','w') as output_file:
		for p in parts:
			output_file.write('\n\n---\n\n# '+p+'\n\n')
			path = p+'.md'
			results += 'Build '+path+'  ...\n'
			text = open(path).read()	
			#print(text)
			output_file.write(text)
	return results


def book_changes(argv):
	'''
	Form the shell script for the commit command.
	'''
	command = 'git status'
	return 'List all pending changes to the book\n' +shell(command)


def book_commit(argv):
	'''
	Form the shell script for the commit command.
	'''
	comment = book_commit_comment(argv)
	command = '''echo Commit all changes from the book project
		git add -A . &&
		git commit -m"%s" &&
		git pull &&
		git push
	''' % comment
	system(command)


def book_commit_comment(argv):
	'''
	Select the comment to tag onto the commit.
	'''
	if len(argv)>2:
		return ' '.join(argv[2:])
	else:
		return 'Automatic book commit'
	

def count_words():
	'''
	Count all of the words in the book
	'''
	system('wc -w book/Book.md')


def book_dired():
	'''Use directory editor in emacs to edit the book content'''
	system('em $book')


def print_index_entry(category, path, title):
	print('- [%s.md, "%s", "%s"]' % (category+'/'+path, category, title))


def book_read_index(name):
	'''Read an index from the book directory'''
	return open(join(environ['book'], name+'.index')).read().split('\n')

def book_index():
	print('site_name: Software Leverage\n\npages:\n')
	for i in book_read_index('Book'):
		print_index_entry('book', i, 'Part '+i)
	for i in book_read_index('Outline'):
		print_index_entry('outline', i, 'Outline '+i)	
	for i in book_read_index('Chapters'):
		print_index_entry('chapters', i, i)	
	# print('book:\n   ', '\n    '.join(book_index('Book')))
	# print('outline:\n   ', '\n    '.join(book_index('Outline')))
	# print('chapters:\n   ', '\n    '.join(book_index('Chapters')))


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


def book_files():
	'''	
	List all of the files in the book using the tree command.
	'''
	print("Get a tree listing of the files")
	system('tree -I env')


def book_help():
	'''
	Show all the book commands and their usage.
	'''
	print('''
    usage: book command [args]
    
    commands:

        changes               -- List doc changes 
        commit [message args] -- Commit all changes to the book
        dired                 -- Edit the book content directory
        edit                  -- Edit the book content
        files                 -- List all of the files
        help                  -- Show the available commands
        list                  -- List the parts of the book
        outline               -- Show the outline for the book
        pdf                   -- Build a PDF file of the book content
        script                -- List the command scripts
        test                  -- Run all system tests
        words                 -- Count the words
			''')


def nested_list(name, children):
	'''Build a string that is a formatted list'''
	return '\n'+name+':    \n    '+'\n    '.join(sorted(children))


def book_list():
	'''
	List the parts of the book source code.
	'''
	results = "List the contents of this book\n"
	for d in ['.', 'book', 'outline', 'chapters']:
		book_dir = join(environ['book'],d)
		files = [f for f in listdir(book_dir) if isfile(join(book_dir,f))]
		results += '\n'+d+':    \n    '+'\n    '.join(sorted(files))
	return results


def book_outline():
	#system('cat $book/outline/* > $book/Outline.md')
	results = "Outline of this book\n"
	outline_dir = join(environ['book'],'outline')
	for f in sorted(listdir(outline_dir)):
		path = join(outline_dir,f)
		title = '# Contents %s' % f.replace('.md','')
		results += '\n\n'+title+':\n'+open(path).read()
	outline_file = join(environ['book'],'Outline.md')
	with open(outline_file,'w') as f:
		f.write(results+'\n')
	return results


def book_pdf():
	'''
	Build the PDF file from the Book markdown file.
	'''
	system('''
		rm *.pdf
		pandoc --toc Book.md -o Book.pdf 2> /dev/null
		pandoc --toc Outline.md -o Outline.pdf 2> /dev/null
		ls -s *.pdf
		cp Book.pdf /home/seaman/Dropbox/Shrinking_World/Book
		cp Outline.pdf /home/seaman/Dropbox/Shrinking_World/Book
		echo Read file with:
		echo '     pdf $book/Book.pdf'
		echo '     pdf $book/Outline.pdf'
		''')


def book_script():
	'''
	List the command to work on the book.
	'''
	print("List the contents of this book")
	for d in ('bin',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def book_read():
	'''Read the PDF for the book'''
	system('rbg evince $book/Book.pdf')


def book_show():
	'''Run page server and point the browser to the book.'''
	print("Show the book content in a browswer")

	system('cd ..; rbg mkdocs serve; sleep 3')
	system('web http://127.0.0.1:8000/book/Cover/')


def book_command(argv):
	'''
	Execute all of the book specific commands
	'''
	if len(argv)>1:
		chdir(environ['book'])
		#print(shell('ls -l'))

		if argv[1]=='assemble':
			print(book_assemble())

		elif argv[1]=='changes':
			print(book_changes(argv))

		elif argv[1]=='commit':
			book_commit(argv)

		elif argv[1]=='dired':
			book_dired()

		elif argv[1]=='edit':
			book_edit(argv)

		elif argv[1]=='index':
			book_index()

		elif argv[1]=='list':
			print(book_list())

		elif argv[1]=='outline':
			print(book_outline())

		elif argv[1]=='pdf':
			book_pdf()

		elif argv[1]=='read':
			book_read()

		elif argv[1]=='script':
			book_script()

		elif argv[1]=='show':
			book_show()

		elif argv[1]=='test':
			book_checker()

		elif argv[1]=='words':
			count_words()
		
		else:
			print('No book command found, '+argv[1])
			book_help()
	else:	
		book_help()