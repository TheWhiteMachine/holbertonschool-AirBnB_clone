#!/usr/bin/python3
"""
    This module contains the Console and its methods
"""
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
    """A console class were all the console function it works"""
    prompt = '(hbnb) '
    classesList = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]

    def do_quit(self, arg):
        """ to exit the program"""
        return True

    def do_EOF(self, arg):
        """ to exit the program"""
        return True

    def emptyline(self):
        """avoids an empty line when using enter"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        splitedARG = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif splitedARG[0] in self.classesList:
            newModel = eval(splitedARG[0])()
            print(newModel.id)
            newModel.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id."""
        splitedARG = arg.split()
        if len(splitedARG) < 1:
            print("** class name missing **")
        elif splitedARG[0] not in self.classesList:
            print("** class doesn't exist **")
        elif len(splitedARG) < 2:
            print("** instance id missing **")
        else:
            class_and_id = splitedARG[0] + '.' + splitedARG[1]
            objects = storage.all()
            if class_and_id in objects:
                print(objects[class_and_id])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file)."""
        splitedARG = arg.split()
        if len(splitedARG) < 1:
            print("** class name missing **")
        elif splitedARG[0] not in self.classesList:
            print("** class doesn't exist **")
        elif len(splitedARG) < 2:
            print("** instance id missing **")
        else:
            class_and_id = splitedARG[0] + '.' + splitedARG[1]
            objects = storage.all()
            if class_and_id in objects:
                del objects[class_and_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name."""
        splitedARG = arg.split()
        my_list = []
        objects = storage.all()
        if not arg:
            for obj in objects:
                my_list.append(str(objects[obj]))
            print(my_list)
        else:
            if splitedARG[0] in self.classesList:
                for obj in objects:
                    if obj.split('.')[0] == splitedARG[0]:
                        my_list.append(str(objects[obj]))
                print(my_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""
        if not arg or len(arg) <= 0:
            print("** class name missing **")
            return
        splitedARG = arg.split()
        if splitedARG[0] not in self.classesList:
            print("** class doesn't exist **")
            return
        elif len(splitedARG) < 2:
            print("** instance id missing **")
            return
        dictionary = storage.all()
        class_and_id = splitedARG[0] + '.' + splitedARG[1]
        if class_and_id not in dictionary:
            print("** no instance found **")
            return
        if len(splitedARG) < 3:
            print("** atribute name missing **")
            return
        elif len(splitedARG) < 4:
            print("** value missing **")
            return
        for key, value in dictionary.items():
            if key == class_and_id:
                setattr(value, splitedARG[2], eval(splitedARG[3]))
                value.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
