#!/usr/bin/python

# Create a single character reader
class GetChar:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# Read one character with a prompt
def readchar (prompt):
    print prompt,	
    getch = GetChar()
    return getch()


# usage:
#    c = readchar('? ')
#    print c



