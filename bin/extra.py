from sys import argv
from os import system,environ
from os.path import join

from outline import extract_headings, convert_to_outline


def extra_edit(topics):
	if topics:
		system('e $book/extra/'+topics[0]+'.md')
	else:
		system('e $book/extra')


def extra_show(topics):
	print('extra show '+str(topics))
	if topics:
		system('cat $book/extra/'+topics[0]+'.md')
	else:
		system('wc -w $book/extra/*')


def extra_outline(topic):
    '''Build a new outline from the book text'''
    path = join(join(environ['book'],'chapters'), topic+'.md') 
    outline = convert_to_outline(extract_headings(open(path).read()))
    print(outline)
   

def extra_command(argv):
	if len(argv)>1:
		if argv[1]=='edit':
			extra_edit(argv[2:])
		elif argv[1]=='outline':
			extra_outline(argv[2:])
	else:
		extra_show(argv[1:])


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    extra_command(argv)