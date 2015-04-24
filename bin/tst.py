#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv


def tst_add(argv):
	'''	
	Create a new tst.
	'''
	print("Add new tst:"+argv[2])
	tst = argv[2]
	path = join(environ['pb'],'%s_test.py' % tst)
	path2 = join(environ['pb'],'prototypetest.py')
	test_content = open(path2).read().replace('prototype',tst)
	#print('Content: %s_test.py \n %s' % (tst,test_content))
	with open(path,'w') as f:
		f.write(test_content)
	tst_edit(argv)


def tst_delete(argv):
	'''	
	Delete the tst.
	'''
	print("Delete tst:",argv[2])
	system('rm  bin/%s_test.py' % argv[2])


def tst_edit(argv):
	'''	
	Edit the content of a tst.
	'''
	print("tst:",argv[2])
	system('e bin/%s_test.py' % argv[2])


def tst_help():
	'''
	Show all the tst tsts and their usage.
	'''
	print('''
	usage: cmd tst [args]

    tst:

        add     [file] -- Add a new tst
        delete  [file] -- Delete a tst
        edit    [file] -- Edit the tst
        list    [file] -- List all tsts
        show    [file] -- Show a tst
      
			''')


def tst_list(argv):
	'''
	List the parts of the tst source code.
	'''
	print("List the contents of this tst")
	for d in ('bin',):
		print(d+':')
		files = listdir(join(environ['p'],d))
		files = [ x for x in files if x.endswith('_test.py') ]
		print('    '+'\n    '.join(files))


def tst_show(argv):
	'''	
	Show the content of a tst.
	'''
	print("tst:",argv[2])
	system('cat bin/%s' % argv[2])


def tst_tst(argv):
	'''
	Execute all of the tst specific tsts
	'''
	if len(argv)>1:

		if argv[1]=='add':
			tst_add(argv)
			exit(0)

		if argv[1]=='delete':
			tst_delete(argv)
			exit(0)

		if argv[1]=='edit':
			tst_edit(argv)
			exit(0)

		if argv[1]=='list':
			tst_list(argv)
			exit(0)

		if argv[1]=='show':
			tst_show(argv)
			exit(0)

		print('No tst tst found, '+argv[1])
		
	tst_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	tst_tst(argv)