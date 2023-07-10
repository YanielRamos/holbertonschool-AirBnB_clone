#!/usr/bin/python3
"""
Entry point for the Console module of Airbnb.
Starts the command line interpreter.
"""
# Import cmd for command line interpreter.
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


# Creating class HBNBCommand
class HBNBCommand(cmd.Cmd):

    # sets custom prompt for the console.
    prompt = '(hbnb) '

    # Dictionary of available classes
    All_Classes = {"BaseModel": BaseException, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the progaram"""
        return True

    def create(self, arg):
        """
        Creates new instances of BaseModel
        saves it and prints the ID
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.All_Classes:
            print("** class doens't exist **")
        else:
            New_Instance = self.All_Classes[args[0]]()
            New_Instance.save()
            print(New_Instance.id)

    def show(self, arg):
        """
        Prints a string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.All_Classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            Llave = args[0] + "." + args[1]
            if Llave not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[Llave])  # Prints the Instance

    def destroy(self, arg):
        """
        Deletes instances depending on the class
        and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name is missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in self.All_Classes:
            print("** class doesn't exist **")
        else:
            Llave = args[0] + "." + args[1]
            if Llave not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(Llave)
                storage.save()

    def do_all(self, arg):
        """
        Prints a string representation of all instances
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in self.All_Classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if args[0] in k])

    def do_update(self, arg):
        """
        Updates instances based on class name and is
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.All_Classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:

            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.all([key].save())


if __name__ == '__main__':
    """
    Used only when this file is not imported
    """
    HBNBCommand().cmdloop()
