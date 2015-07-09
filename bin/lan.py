#!/usr/bin/env python

from os import system, listdir, environ
from os.path import join
from sys import argv

from lan_test import lan_checker


def lan_host(ip):
    '''Show the host for an ip address on lan'''
    print("Hostname : "+ip)
    system('ssh %s hostname ' % ip)


def lan_list():
    '''List all known lans ports'''
    print('''lan list:

        DLink           10.0.0.1
        seaman-server   10.0.0.19
                        10.0.0.20
                        10.0.0.26
                        
        Netgear50       172.16.0.1
        seaman-mini     172.16.0.2
        seaman-macbook  172.16.0.4
                        172.16.0.8
        seaman-hammer   172.16.0.16
                        172.16.0.20

          ''')


def lan_help():
    '''Show all the lan lans and their usage.'''
    print('''
    usage: lan cmd [args]

    lan:

        host  ip    -- Show the host for an ip address on lan
        list        -- List all known lans ports
        ping  ip    -- Ping a lan address
        scan        -- Scan for machines on network
        ssh   ip    -- Edit the lan
        test        -- Self test
      
            ''')


def lan_ping(ip):
    system('ping '+ip)


def lan_scan():
    '''Scan for machines on network'''
    system('networkscan')


def lan_command(argv):
    '''Execute all of the lan specific lans'''
    if len(argv)>1:

        if argv[1]=='host':
            lan_host(argv[2])

        elif argv[1]=='ping':
            lan_ping(argv[2])

        elif argv[1]=='list':
            lan_list()

        elif argv[1]=='scan':
            lan_scan()

        elif argv[1]=='test':
            lan_checker()

        else:
            print('No lan command found, '+argv[1])
            lan_help()
    else:
        print('No arguments given')
        lan_help()


'''
Create a script that can be run from the shell
'''
if __name__=='__main__':
    lan_command(argv)