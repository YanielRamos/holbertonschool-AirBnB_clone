#!/usr/bin/python3

import cmd

"""
Creating class HBNBCommand
"""


class HBNBCommand(cmd.Cmd):
    """
    Class of HBNBCommand
    """
    prompt = '(hbnb)'

    def _quit(self, arg):
        """
        Exits the program
        """
        return True

    def _EOF(self, arg):
        """
        Exit the progaram
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
