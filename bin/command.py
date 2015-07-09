#!/usr/bin/python3
# Create a new python command script

from os import environ, system
from os.path import exists,join
from sys import argv


script = '''#!/usr/bin/python3
# comment


print("comment")

code

'''

# Edit the file
def cmd_new(f, comment='No comment', code='No Code'):
    path = join(environ['pb'],f)
    if exists(path):
        print ("File already exists, "+path)
    else:
        print ("New command file, "+path)
        text = script.replace('comment',comment).replace('code', code)
        open(path, 'w').write(text)
        system('chmod 755 '+path)
    system ('cmd-edit '+f)
  

# When run stand alone then do the test
if __name__ == "__main__":
    if len(argv)>1:
        if len(argv)>2:
            if len(argv)>3:
                cmd_new(argv[1], argv[2], argv[3])
            else:
                cmd_new(argv[1], argv[2])
        else:
            cmd_new(argv[1])
    else:
        print ('Need a file')


  
