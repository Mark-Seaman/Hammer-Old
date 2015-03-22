
# REPL for Jack Script
def jack_script():
    print ('Jack Hammer Script Commander:')
    while True:
        s = input('>')
        if not s or s=='exit':
            print ('Good bye')
            exit(0)
        print ('s = %s'%s)


jack_script()
