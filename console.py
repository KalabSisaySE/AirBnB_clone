#!/usr/bin/python3
"""defines a command interpreter for managing creation of objects"""
import cmd

from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

MODELS = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]


class HBNBCommand(cmd.Cmd):
    """interprets commands for managing models"""

    prompt = "(hbnb) "

    def parse_args(self, line):
        """extracts the arguments and pass it to the handler"""
        args = []
        if '"' in line:
            trimmed_line = line.strip()
            is_double_quote_arg = False
            arg = ""

            for char in trimmed_line:
                if is_double_quote_arg or char != " ":
                    arg += char

                if not is_double_quote_arg and char == '"':
                    is_double_quote_arg = True
                elif is_double_quote_arg and char == '"':
                    args.append(arg)
                    is_double_quote_arg = False
                    arg = ""
                elif not is_double_quote_arg and char == " ":
                    if arg:
                        args.append(arg)
                    arg = ""

            if arg:
                args.append(arg)
        else:
            args = line.split()

        return args

    def check_and_convert(self, val):
        """returns int or float of a string if convertible"""
        try:
            return int(val)
        except ValueError:
            try:
                return float(val)
            except ValueError:
                return val.replace("'", "").replace('"', "")

    def emptyline(self):
        """prevents empty from executing previous command"""
        pass

    def do_EOF(self, line):
        """exits the interpreter"""
        return True

    def do_quit(self, line):
        """exits the interpreter"""
        return True

    def do_create(self, line):
        """creates a new instance of the given model"""
        args = self.parse_args(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in MODELS:
            print("** class doesn't exist **")
        else:
            obj = eval(f"{args[0]}()")
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """prints the string representation of the instance with the given model and id"""
        args = self.parse_args(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in MODELS:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if f"{args[0]}.{args[1]}" in storage.all():
                print(storage.all().get(f"{args[0]}.{args[1]}"))
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance with the given model and id"""
        args = self.parse_args(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in MODELS:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if f"{args[0]}.{args[1]}" in storage.all():
                del storage.all()[f"{args[0]}.{args[1]}"]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """prints all string representation of all or specific model instances"""
        args = self.parse_args(line)
        objs = []
        if args:
            if args[0] not in MODELS:
                print("** class doesn't exist **")
            else:
                for key, obj in storage.all().items():
                    if key.startswith(args[0]):
                        objs.append(str(obj))
        else:
            objs = [str(obj) for key, obj in storage.all().items()]

        if objs:
            print(objs)

    def do_update(self, line):
        """updates an instance's attribute based on the model and id"""
        args = self.parse_args(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in MODELS:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if f"{args[0]}.{args[1]}" not in storage.all():
                print("** no instance found **")
            else:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    attr_name = args[2]
                    attr_value = self.check_and_convert(args[3])
                    obj = storage.all()[f"{args[0]}.{args[1]}"]
                    setattr(obj, attr_name, attr_value)
                    obj.save()

    def help_quit(self):
        """prints the help doc for the command `quit`"""
        print("Quit command to exit the program")

    def help_create(self):
        """print the help doc for the command `create`"""
        print(
            "Creates a new instance of the given model. \n\tUsage: <create BaseModel>"
        )

    def help_show(self):
        """print the help doc for the command `show`"""
        help_doc = (
            "Displays the string representation of the "
            "instance with the given model and id."
            "\n\tUsage: <show BaseModel 1234-1234-1234>"
        )
        print(help_doc)

    def help_destroy(self):
        """print the help doc for the command `destroy`"""
        help_doc = (
            "Deletes the instance with the given model and id."
            "\n\tUsage: <destroy BaseModel 1234-1234-1234>"
        )
        print(help_doc)

    def help_all(self):
        """print the help doc for the command `all`"""
        help_doc = (
            "Displays the string representation of the all"
            " instances or specific model instances"
            " depending on the second argument"
            "\n\tUsage: <all> <all BaseModel>"
        )
        print(help_doc)

    def help_update(self):
        """print the help doc for the command `update`"""
        help_doc = (
            "Updates the instance with the given model and id"
            " instances or specific model instances"
            "\ndepending on the second argument"
            '\n\tUsage: <update BaseModel 1234-1234-1234 email "aibnb@mail.com">'
        )
        print(help_doc)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
