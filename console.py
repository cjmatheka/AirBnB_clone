#!/usr/bin/env python3

""" AirBnB Clone Console """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place, "Review": Review
    }

    def do_create(self, arg):
        """
        Creates a new instance, saves it and prints the id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        try:
            new_instance = self.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(f"** Error creating instance: {e} **")

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        print_list = []
        if not arg:
            for value in storage.all().values():
                print_list.append(str(value))
        else:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if arg in key:
                    print_list.append(str(value))

        print('\n'.join(print_list))

    def do_update(self, arg):
        """Updates an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = storage.all()[key]
        try:
            attr_type = type(getattr(obj, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass  # Attribute doesn't exist; add it

        setattr(obj, args[2], args[3])
        obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print("")  # Print a new line
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
