#!/usr/bin/python3
# Create a new python command script

from os import environ, system

def mini():
    return environ['macmini']

def rsync(fromdir,todir):
  system ('rsync -auv '+fromdir+'/ ' + todir)


def file_copy_to_mini(argv):
    if not len(argv)==2 :
        print ('usage: file-to-mini <dir>')
        exit(1)


    # system ('rsync -auv ~/'+argv[1] + '/ ' + mini() + ':' + argv[1])
    rsync ('~/'+argv[1] + '/', mini() + ':' + argv[1])

def file_copy_from_mini(argv):
    if not len(argv)==2 :
        print ('usage: file-from-mini <dir>')
        exit(1)

    rsync (mini() + ':' + argv[1] + '/', '~/'+argv[1])



