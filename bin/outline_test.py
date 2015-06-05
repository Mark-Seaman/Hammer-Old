from tst import run_diff_checks, shell, lines, limit_lines


	

def outline_test():
	return shell('outline') + shell('outline outline')
	

def outline_diff_test():
	return limit_lines('outline diff', 250,300)


def outline_headings_test():
	return shell('outline headings')
	

def outline_index_test():
	return limit_lines ('outline index', 900,1000)


def outline_show_test():
	return shell('outline show')
	

def outline_checker():
	'''Execute all the desired diff tests'''
	my_tests = {
		'outline': outline_test,
		'outline-diff': outline_diff_test,
        'outline-headings': outline_headings_test,
        'outline-index': outline_index_test,
        'outline-show': outline_show_test,
    }
	run_diff_checks('outline', my_tests)


# Create a script that can be run from the tst
if __name__=='__main__':
    outline_checker()