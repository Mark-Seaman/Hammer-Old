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
	if topics:
		system('cat $book/extra/'+topics[0]+'.md')
	else:
		system('wc -w $book/extra/*')


def read_extra(topic):
    '''Read extra chapter text'''
    chapter_dir = join(environ['book'],'chapters')
    path = join(chapter_dir,topic+'.md')
    return open(path).read()


def extra_outline(topic):
    '''Build a new outline from the book text'''
    headings = extract_headings(read_extra(topic))
    print(convert_to_outline(headings))
   

def extra_command(argv):
	if len(argv)>2:
		if argv[1]=='edit':
			extra_edit(argv[2])
		elif argv[1]=='outline':
			extra_outline(argv[2])
	if len(argv)>1:
		pass
	else:
		extra_show(argv[1:])


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    extra_command(argv)