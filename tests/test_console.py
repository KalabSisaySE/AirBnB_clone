#!/usr/bin/python3
"""tests for the command interpreter"""
import unittest

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """tests for the command interpreter"""

    def test_interpreter_prompt(self):
        """tests the interpreter prompt name"""
        interpreter = HBNBCommand()
        print(interpreter.prompt)
        self.assertTrue(interpreter.prompt.startswith("(hbnb)"))
