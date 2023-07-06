#!/usr/bin/env python3
"""Entry point module of the Command
interpreter
"""
# Importing cmd for command line interpreter.
import cmd
import shlex
import models
import sys
from models import storage
from models.base_model import BaseModel

# Dictionary of classes available
All_Classes = {"BaseModel": BaseModel}

"""
Creating class HBNBCommand
"""


class HBNBCommand(cmd.Cmd):

    # sets custom prompt for the console.
    prompt = '(hbnb) '

    # Define available clases.
    def __init__(self):
        super(HBNBCommand, self).__init__()
        self.All_Classes = {"BaseModel": BaseModel}

    # Command 'quit' exit the program
    def _quit(self, arg):
        """
        Exit the program
        """
        # Verify if running in non-interactive mode
        if not sys.stdin.isatty():
            # print a newline character
            print()
            # If 'quit' is exectued, the loop ends
        return True

    def _EOF(self, arg):
        """
        Exit the progaram
        """
        # Exits the same way 'quit' does
        return self._quit(args)

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        # If newline is empty do nothing
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
