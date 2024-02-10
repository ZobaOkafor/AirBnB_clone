#!/usr/bin/python3
"""
Moduleconsole.py - Entry point for the command interpreter.
"""

import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class - Command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is reached.
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def help_quit(self):
        """
        Display help message for quit command.
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """
        Display help message for EOF command.
        """
        print("Exit the program when EOF is reached.\n")

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.
        Usage: all [class_name]
        """
        args = arg.split()
        obj_list = []
        if not arg:
            for obj in stroage.all().value():
                obj_list.append(str(obj))
            print(obj_list)
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        for key in storage.all():
            if args[0] == key.split('.')[0]:
                obj_list.append(str(storage.all()[key]))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class_name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if hasattr(storage.all()[key], args[2]):
            setattr(storage.all()[key], args[2], args[3])
            storage.all()[key].save()
        else:
            print("** no instance found **")

    def default(self, arg):
        """
        Default method to handle <class name>.count(), <class name>.show(<id>),
        <class name>.destroy(<id>), and
        <class name>.update(<id>, <dictionary representation>).
        """
        args = arg.split(".")
        if len(args) < 2:
            print("*** Unknown syntax: {}".format(arg))
            return False
        class_name = args[0]
        command = args[1].split("(")[0]
        if command == "all":
            self.do_all(class_name)
        elif command == "count":
            count = 0
            for key in storage.all():
                if class_name == key.split('.')[0]:
                    count += 1
            print(count)
        elif command == "show":
            instance_id = args[1].split("(")[1].strip('")')
            self.do_show("{} {}".format(class_name, instance_id))
        elif command == "destroy":
            instance_id = args[1].split("(")[1].strip('")')
            self.do_destroy("{} {}".format(class_name, instance_id))
        elif command == "update":
            update_args = args[1].split("(")[1].strip('")').split(", ")
            instance_id = update_args[0]
            attribute = update_args[1]
            value = update_args[2].strip('")')
            self.do_update("{} {} {} {}".format(class_name, instance_id,
                                                attribute, value))
        else:
            print("*** Unknown syntax: {}".format(arg))


if__name__ = '__main__':
    HBNBCommand().cmdloop()
