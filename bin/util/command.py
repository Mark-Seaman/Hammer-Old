#!/usr/bin/env python
# Command master program

from os         import system, environ, chdir
from os.path    import join
from argparse   import ArgumentParser


# Parse all of the command line arguments
def arg_parser():
    parser = ArgumentParser(description="Test control program")
    parser.add_argument("-unit")
    parser.add_argument("-milldo")
    parser.add_argument("-millget")
    parser.add_argument("-millput")
    parser.add_argument("-svrdo")
    parser.add_argument("-svrget")
    parser.add_argument("-svrput")
    parser.add_argument("-eachmilldo")
    parser.add_argument("-eachmillget")
    parser.add_argument("-eachmillput")
    return parser
 
# Test API
def run_command():
    parser = arg_parser()
    args   = parser.parse_args()

    if args.milldo and args.unit:
        print ('sc-milldo %s %s'%(args.unit,args.milldo))
        return

    if args.millget and args.unit:
        print ('sc-millget %s %s'%(args.unit,args.millget))
        return

    if args.millput and args.unit:
        print ('sc-millput %s %s'%(args.unit,args.millput))
        return

    if args.svrdo and args.unit:
        print ('sc-do %s %s'%(args.unit,args.svrdo))
        return

    if args.svrget and args.unit:
        print ('sc-get %s %s %s'%(args.unit,args.svrget,args.svrget))
        return

    if args.svrput and args.unit:
        print ('sc-get %s %s %s'%(args.unit,args.svrput,args.svrput))
        return

     if args.eachmilldo and args.unit:
        print ('each-mill sc-milldo UNIT %s'%(args.eachmilldo))
        return

      if args.eachmillget and args.unit:
        print ('each-mill sc-millget UNIT %s'%(args.eachmillget))
        return

      if args.eachmillput and args.unit:
        print ('each-mill sc-millput UNIT %s'%(args.eachmillput))
        return

    print parser.print_help()
    #system ('rbg /opt/google/chrome/google-chrome --incognito')
#, action="store_true")

# Open the data store and perform the requested command
run_command()

