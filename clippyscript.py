#!/bin/python

from subprocess import call
from random import randint, seed
from time import ctime # for seeding

if __name__ == "__main__":
    seed(ctime())
    import sys

    r = randint(0,3)
    message0 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like to install Pulse Audio?")
    message1 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like to delete the root directory?")
    message2 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like help writing a letter?")
    message3 = ("Hi, I'm Clippy, your shell assisstant. Command not found:\n\n" + sys.argv[1] + "\n\nWould you like me to reboot your computer?")

    if r == 0:
        call(['cowsay', '-fclippy', message0])
    elif r == 1:
        call(['cowsay', '-fclippy', message1])
    elif r == 2:
        call(['cowsay', '-fclippy', message2])
    elif r == 3:
        call(['cowsay', '-fclippy', message3])
