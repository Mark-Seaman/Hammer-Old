#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ, chdir
from os.path import join, isdir
from re import sub,compile,DOTALL,IGNORECASE
from sys import argv
   
from code_test import code_checker
   

def read_source(filename):
	text = open(join(environ['p'],filename)).read()
	return [x for x in text.split('\n') if x.replace(' ','')]


def extract_functions(lines):
	for i,line in enumerate(lines):
		if line.strip().startswith('def'):
			pat = compile(r"\s*def (.*)\s*\(.*")
			name = pat.sub(r'\1',line)
			yield ((i,name))
	yield((i,''))


def function_sizes():
	for filename in python_source():
		total_cost = 0
		lines = read_source(filename)
		summary = ''
		name = None
		for x in extract_functions(lines):
			if name:
				num_lines = x[0]-start
				cost = num_lines ** 1.2 # Exponential penalty of size
				total_cost += cost
				summary += '    %d, %d, %s\n' % (cost, num_lines, name)
				start = x[1]
			name = x[1]
			start = x[0]
		num_lines = len(lines)
		cost = num_lines ** 1.2 # Exponential penalty of size
		total_cost += cost
		print('\n%d - %d - %s\n%s' % (total_cost, len(lines), filename, summary))


def calculate_complexity(filename):
	text = open(join(environ['p'],filename)).read()
	lines = text.split('\n')
	num_imports = len([i for i in lines if 'import' in i])
	import_cost = 10  # Equal to 10 lines of code
	num_lines = len(lines)
	coupling_cost = 1.2 # Exponential penalty of size
	complexity = (num_lines + num_imports * import_cost) ** coupling_cost
	return (num_lines,num_imports,complexity)


def code_complexity(code_dirs=None):
	'''Measure the code complexity'''
	files = code_list(code_dirs).split('\n')
	print ('code_complexity:')
	python_files = [f for f in files if f.endswith('.py')]
	total = (0,0,0)

	print('File                              Lines  Imports Complexity')
	for f in sorted(python_files):
		lines,imports,complexity = calculate_complexity(f)
		total = (total[0]+lines, total[1]+imports, total[2]+complexity)
		print('%-30s %8d %8d %8d' % (f, lines, imports, complexity))

	print('%-30s %8d %8d %8d' % ('Total', total[0], total[1], total[2]))


def code_help():
	'''Show all the code codes and their usage.'''
	print('''
	usage: cmd code [args]

    code:
    	complexity     -- Calculate the complexity of the source code
        list    [file] -- List all codes
        show    [file] -- Show a code
        test           -- Self test
      
			''')


def python_source(iles=None):
	'''Return a list of the python source files'''
	return [f for f in code_source() if f.endswith('.py')]


def code_source(files=None):
	'''List the files of source code.'''
	if not files:
		files = ['bin']
	for d in files:
		chdir(environ['p'])
		files = [f for f in glob(d+'/*') if not isdir(f)]
		files = [f for f in files if not f.endswith('.pyc')]
		if files:
			for f in files:
				yield((f))


def code_list(files=None):
	'''List the files of source code.'''
	results = []
	if not files:
		files = ['bin']
	for d in files:
		chdir(environ['p'])
		files = [f for f in glob(d+'/*') if not isdir(f)]
		files = [f for f in files if not f.endswith('.pyc')]
		if files:
			results.append('\n'.join(files))
	return '\n'.join(results)


def code_show(files):
	'''Show the content of a code.'''
	print("code:",files)
	if not files:
		files = code_list().split('\n')
	for f in files:
		system('cat %s' % f)


def code_command(argv):
	'''Execute all of the code specific codes'''
	if len(argv)>1:

		if argv[1]=='complexity':
			code_complexity()

		if argv[1]=='functions':
			function_sizes()

		elif argv[1]=='list':
			print(code_list())

		elif argv[1]=='show':
			code_show(argv[2:])

		elif argv[1]=='test':
			code_checker()

		else:
			print('No code command found, '+argv[1])
			code_help()
	else:
		print('No arguments given')
		code_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
	code_command(argv)