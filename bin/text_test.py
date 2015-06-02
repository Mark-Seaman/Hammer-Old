from tst import run_diff_checks, shell, lines, limit_lines


def text_test():
	return shell('text')
	

def text_outline_test():
	return shell('text outline')
	
def text_headings_test():
	return shell('text headings')
	

def text_checker():
	'''Execute all the desired diff tests'''
	my_tests = {
		'text': text_test,
        'text-outline': text_outline_test,
        'text-headings': text_headings_test,
    }
	run_diff_checks('doc', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    text_checker()