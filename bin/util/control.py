#!/usr/bin/env python
# Test control program

from os         import system, chdir
from os.path    import join
from argparse   import ArgumentParser


# Parse all of the command line arguments
def parse_args():
    parser = ArgumentParser(description="Test control program")
    parser.add_argument("-list",  action="store_true")
    parser.add_argument("-show", action="store_true")
    parser.add_argument("-add", action="store_true")
    parser.add_argument("-edit",  action="store_true")
    parser.add_argument("-delete",  action="store_true")
    parser.add_argument("-test",  action="store_true")
    parser.add_argument("-run",  action="store_true")
    parser.add_argument("-importfile",  action="store_true")
    parser.add_argument("-exportfile",  action="store_true")
    return parser.parse_args()
 
# Test API
def run_test_command():
    args = parse_args()

    if args.list:
        print 'list'
        return

    if args.show:
        print 'show'
        return

    if args.add:
        print 'add'
        return
        
    if args.edit:
        print 'stop'
        return

    if args.delete:
        print 'delete'
        return

    if args.test:
        print 'test'
        return

    if args.run:
        print 'run'
        return

    if args.importfile:
        print 'importfile'
        return

    if args.exportfile:
        print 'exportfile'
        return

    print 'usage: control'
    #system ('rbg /opt/google/chrome/google-chrome --incognito')


# Open the data store and perform the requested command
run_test_command()

