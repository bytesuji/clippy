#!/bin/python

from subprocess import call
from random import randint, seed
from time import time # for seeding

if __name__ == "__main__":
    seed(time())
    import sys

    r = randint(0,7)

    message0 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like to install Pulse Audio?")
    message1 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like to delete the root directory?")
    message2 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like help writing a letter?")
    message3 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like me to reboot your computer?")
    message4 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like me to pipe myself to /dev/null?")
    message5 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like me to disable your keyboard?")
    message6 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like me to help you tie a noose?")
    message7 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like me to uninstall the Linux kernel?")

    if r == 0:
        call(['cowsay', '-fclippy', message0])
    elif r == 1:
        call(['cowsay', '-fclippy', message1])
    elif r == 2:
        call(['cowsay', '-fclippy', message2])
    elif r == 3:
        call(['cowsay', '-fclippy', message3])
    elif r == 4:
        call(['cowsay', '-fclippy', message4])
    elif r == 5:
        call(['cowsay', '-fclippy', message5])
    elif r == 6:
        call(['cowsay', '-fclippy', message6])
    elif r == 7:
        call(['cowsay', '-fclippy', message7])
