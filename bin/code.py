#!/usr/bin/env python

from glob import glob
from os import system, listdir, environ, chdir
from os.path import join, isdir
from re import sub,compile,DOTALL,IGNORECASE
from sys import argv
   
from code_test import code_checker
   

def read_source(filename):
	'''Read the source code file, remove blanks and split lines'''
	text = open(join(environ['p'],filename)).read()
	return [x for x in text.split('\n') if x.replace(' ','')]


def extract_functions(lines):
	'''Extract all of the functions from the source and count their length'''
	start = 0
	for i,line in enumerate(lines):
		if line.strip().startswith('def'):
			pat = compile(r"\s*def (.*)\s*\(.*")
			name = pat.sub(r'\1',line)
			yield ((i-start,name))
			start = i
	yield((i-start,''))


def function_cost(name,size):
	cost = size ** 1.3  # Exponential penalty of size
	details = '    %-26s %8d %8d\n' % (name, size, cost)
	return cost,details


def module_cost(lines):
	module_cost = 0
	summary = '\n'
	name = 'module'
	
	for x in extract_functions(lines):		
		cost,details = function_cost(name, x[0])
		summary += details
		module_cost += cost
		name = x[1]

	size = len(lines)
	cost = (size/2) ** 1.1 # Exponential penalty of size
	module_cost += cost
	return module_cost,summary
	

def complexity(filename, lines, show_functions):
	num_lines = len(lines)
	cost, summary = module_cost(lines)
	if show_functions:	
		print('%-30s %8d %8d %s' % (filename, num_lines, cost, summary))
	else:
		print('%-30s %8d %8d' % (filename, num_lines, cost))
	return (num_lines, cost, summary)


def system_complexity(source, show_functions):
	total_cost = 0
	total_lines = 0
	for filename in python_source():
		lines = read_source(filename)
		num_lines, cost, summary = complexity(filename, lines, show_functions)
		total_lines += num_lines
		total_cost += cost
	return (total_lines, total_cost)	


def function_sizes(show_functions = False):
	'''Measure the complexity based on the function sizes within the module'''
	print('File                              Lines  Complexity\n')
	total_lines, total_cost = system_complexity(python_source(), show_functions)
	print('\n%-30s %8d %8d' % ('    total', total_lines, total_cost))


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


def python_source(files=None):
	'''Return a list of the python source files'''
	return [f for f in code_source(files) if f.endswith('.py')]


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
		files = [f for f in glob(d+'/*.py') if not isdir(f)]
		files = [f for f in files if not f.endswith('_test.py')]
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
			function_sizes()

		elif argv[1]=='functions':
			function_sizes(True)

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
