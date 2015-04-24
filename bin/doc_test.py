'''
Document Tests
---------------

Run all of the tests that are available.  Output the test results.

'''

from os import listdir, environ, system
from os.path import join

#from formatter import map_muse_to_markdown, map_markdown_to_muse


def count_lines(filepath, min=None, max=None):
	num_lines_output = len(open(filepath).read().split('\n'))
	print('Count lines %s: %d' % (filepath, num_lines_output))
	if min:
		print('Min count lines %s: actual=%d, min=%d' % (filepath, num_lines_output, min))
		assert(num_lines_output>=min)
	if max:
		print('Max count lines %s: actual=%d, max=%d' % (filepath, num_lines_output, max))
		assert(num_lines_output<=max)


def nose_test():
	assert(True)


# def assemble_doc_test():
# 	system('bo assemble > /dev/null')
# 	count_lines('docs/doc/doc.md', 870, 900)


def doc_file_test():
	system('ls $pd > /tmp/doc-files')
	count_lines('/tmp/doc-files', min=4, max=5)


def bin_file_test():
	num_files = len(listdir(join(environ['pb'])))
	print('bin_file_test',num_files)
	assert (14==num_files)


# def markdown_convert_test():
# 	md = '''
# * Heading 1
# ** Heading 2
# **Bold** this is plain
#  * List item
#  my link [[http://Shrinking-World.org][Shrinking World Solutions]] more text
#  my link [[http://Shrinking-World.org]] more text
# '''.split('\n')

# 	muse = '''
# # Heading 1
# ## Heading 2
# **Bold** this is plain
# * List item
#  my link [Shrinking World Solutions](http://Shrinking-World.org.md) more text
#  my link [http://Shrinking-World.org](http://Shrinking-World.org.md) more text
# '''

# 	answer = '\n'.join([map_muse_to_markdown(x) for x in md])
# 	print ('answer: ',answer)
# 	print ('expected: ',muse)
# 	assert(answer==muse)


# def muse_convert_test():
# 	muse = '''
# # Heading 1
# ## Heading 2
# **Bold** this is plain
# * List item
#  my link [Shrinking World Solutions](http://Shrinking-World.org) more text
#  my link [[Shrinking World Solutions]] more text
# '''.split('\n')

# 	md = '''
# * Heading 1
# ** Heading 2
# **Bold** this is plain
#  * List item
#  my link [[http://Shrinking-World.org][Shrinking World Solutions]] more text
#  my link [[Shrinking World Solutions]] more text
# '''

# 	answer = '\n'.join([map_markdown_to_muse(x) for x in muse])
# 	print ('answer: ',answer)
# 	print ('expected: ',md)
# 	assert(answer==md)


def command_test():
	system('''{ 
		doc files
		doc help
		} > /tmp/doc-test''')
	count_lines('/tmp/doc-test', min=80, max=90)
	

