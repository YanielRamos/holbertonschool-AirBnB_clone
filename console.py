#!/usr/bin/env python3
"""Entry point module of the 
Command interpreter"""
# Import cmd for command line interpreter.
import cmd
import shlex
import models
import sys
from models import storage
from models.base_model import BaseModel


# Dictionary of classes available
classes = {"BaseModel": BaseModel}


# Creating class HBNBCommand
class HBNBCommand(cmd.Cmd):

    # sets custom prompt for the console.
    prompt = '(hbnb) '

    # Define available clases.
    def __init__(self):
        super(HBNBCommand, self).__init__()
        self.classes = {"BaseModel": BaseModel}

    # Command 'quit' exit the program
    def do_quit(self, args):
        """Exit the program"""
        # Verify if running in non-interactive mode
        if not sys.stdin.isatty():
            # print a newline character
            print()
            # If 'quit' is exectued, the loop ends
        return True

    # Command 'EOF' exit program
    def do_EOF(self, args):
        """Exit the progaram"""
        # Exits the same way 'quit' does
        return self.do_quit(args)

    # if line is empty, do nothing
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        # If newline is empty do nothing
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
