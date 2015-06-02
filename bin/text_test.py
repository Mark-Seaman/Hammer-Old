from tst import run_diff_checks, shell, lines, limit_lines


def text_test():
	return shell('text')
	

def text_outline_test():
	return shell('text outline')
	

def text_headings_test():
	return shell('text headings')
	
def text_index_test():
	return limit_lines ('text index', 450,460)

def text_show_test():
	return shell('text show')
	

def text_checker():
	'''Execute all the desired diff tests'''
	my_tests = {
		'text': text_test,
        'text-outline': text_outline_test,
        'text-headings': text_headings_test,
        'text-index': text_index_test,
        'text-show': text_show_test,
    }
	run_diff_checks('text', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    text_checker()