#!/usr/bin/python3
"""
The console wich controls the entire C.R.U.D process
using the CMD Module which is used to create a simple
python interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The console which would be controlling the backend of the project.
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        Specifies the end of file and terminates
        the program by pressing <CTRL + D>
        """
        return True

    def postloop(self):
        """
        Creates an emptyline when EOF is called
        but it affects the do_quit when the quit
        is called by creating an extra new-line
        when it is called. 
        """
        print()

    def emptyline(self):
        """
        Handles empty line input when '\n' is passed
        as an argument in the console.
        """
        pass

    def do_quit(self, line):
        """Terminates the console and exits with a new line
        <quit>
        """
        return True

    def help_quit(self):
        print("Terminates the console and exit")

    def do_create(self, line):
        """
        Creates new user for BaseModel and then prints the ID of the
        new instances
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line_name, line_id):
        if not line_name:
            print("** class name missing **")
        if line_name != "BaseModel":
            print("** class doesn't exist **")
        new_vars = storage.all()
        for key, values in new_vars.keys():
            class_name, instance_id = key.split('.')
            # instance_id = str(instance_id)
            if class_name == line_name and instance_id == line_id:
                print(new_vars[class_name](instance_id))
            print(key)

    def do_delete(self, line_name, line_id):
        if not line_name:
            print("** class name missing **")
        elif line_name != "BaseModel":
            print("** class doesn't exist **")
        elif not line_id:
            print("** instance id missing **")

    def do_all(self, line_name):
        """
        Prints all values in BaseModel by accessing
        the storage(JSON File) and then convert it to string
        then append the value into an empty list
        """
        if line_name and line_name != "BaseModel":
                print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            empty_list = []
            for obj_id in all_objs.values():
                empty_list.append(str(obj_id))
            print(empty_list)

    def do_update(self, line_name, line_id):
            pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
