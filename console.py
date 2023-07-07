#!/usr/bin/python3
""""
    This module contains the Console
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A console class were all the console function it works"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        return True
    def do_EOF(self, arg):
        return True
    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()