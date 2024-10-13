#!/usr/bin/python3
"""defines a command interpreter for managing creation of objects"""
import cmd


class HBNBCommand(cmd.Cmd):
    """interprets commands for managing models"""

    prompt = "(hbnb) "

    def emptyline(self):
        """prevents empty from executing previous command"""
        pass

    def do_EOF(self, args):
        """exits the interpreter"""
        return True

    def do_quit(self, args):
        """exits the interpreter"""
        return True

    def help_quit(self):
        """prints the help doc for the command `quit`"""
        print("Quit command to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
