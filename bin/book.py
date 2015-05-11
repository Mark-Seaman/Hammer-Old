from os import system, listdir, environ, chdir
from os.path import join
from sys import argv

from tst import shell
from book_test import book_checker


def assemble_book_parts():
	'''
	Put together a markdown file from the individual parts
	'''
	results = 'Assemble: Index.md\n'
	parts = ('book/Cover', 'book/Abstract', 'book/Intro', 'book/Outline', 
		'chapters/Part1', 'chapters/Part2', 'chapters/Part3', 'chapters/Part4',
		'chapters/Part5', 'book/10Ways')
	with open('Book.md','w') as output_file:
		for p in parts:
			output_file.write('\n\n---\n\n# '+p+'\n\n')
			path = p+'.md'
			results += 'Build '+path+'  ...\n'
			text = open(path).read()	
			#print(text)
			output_file.write(text)
	return results


def doc_changes(argv):
	'''
	Form the shell script for the commit command.
	'''
	command = 'git status'
	return 'List all pending changes to the book\n' +shell(command)


def doc_commit(argv):
	'''
	Form the shell script for the commit command.
	'''
	comment = doc_commit_comment(argv)
	command = '''echo Commit all changes from the book project
		git add -A . &&
		git commit -m"%s" &&
		git pull &&
		git push
	''' % comment
	system(command)


def doc_commit_comment(argv):
	'''
	Select the comment to tag onto the commit.
	'''
	if len(argv)>1:
		return ' '.join(argv[2:])
	else:
		return 'Automatic book commit'
	

def count_words():
	'''
	Count all of the words in the book
	'''
	system('wc -w book/Book.md')


def create_book_pdf():
	'''
	Build the PDF file from the Book markdown file.
	'''
	system('''
		rm Book.pdf; 
		pandoc --toc book/Book.md -o Book.pdf 2> /dev/null; 
		ls -l Book.pdf
		cp Book.pdf /home/seaman/Dropbox/Shrinking_World/Book
		''')


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
        files                 -- List all of the files
        help                  -- Show the available commands
        list                  -- List the parts of the book
        pdf                   -- Build a PDF file of the book content
        script                -- List the command scripts
        test                  -- Run all system tests
        words                 -- Count the words
			''')


def book_list():
	'''
	List the parts of the book source code.
	'''
	results = "List the contents of this book\n"
	for d in ['.', 'book', 'chapters']:
		book_dir = join(environ['book'],d)
		results += d+':    \n'+'\n    '.join(listdir(book_dir))
	return results


def book_outline():
	results = "Outline of this book\n"
	outline_dir = join(environ['book'],'outline')
	for f in listdir(outline_dir):
		path = join(outline_dir,f)
		results += '\n\n# '+path+':\n'+open(path).read()
	return results


def book_script():
	'''
	List the command to work on the book.
	'''
	print("List the contents of this book")
	for d in ('bin',):
		print(d+':')
		print('    '+'\n    '.join(listdir(join(environ['p'],d))))


def book_show():
	'''
	Show the pages of the book.  Start the server and point the browser to the page.
	'''
	print("Show the book content in a browswer")

	system('rbg mkdocs serve; sleep 3')
	system('web http://127.0.0.1:8000/book/Cover/')


def book_command(argv):
	'''
	Execute all of the book specific commands
	'''
	if len(argv)>1:
		chdir(environ['book'])
		#print(shell('ls -l'))

		if argv[1]=='assemble':
			print(assemble_book_parts())

		elif argv[1]=='changes':
			print(doc_changes(argv))

		elif argv[1]=='commit':
			doc_commit(argv)

		elif argv[1]=='files':
			book_files()

		elif argv[1]=='list':
			print(book_list())

		elif argv[1]=='outline':
			print(book_outline())

		elif argv[1]=='pdf':
			create_book_pdf()

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