#!/usr/bin/python3
"""
The console wich controls the entire C.R.U.D process
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
        specifies the end of file and terminates
        the program by pressing <CTRL + D>
        """
        return True

    def postloop(self):
        print()

    def emptyline(self):
        """
        handles empty line input when '\n' is passed
        as an argument in the console
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
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line_name, line_id):
        new_vars = storage.all()
        for key, values in new_vars.items():
            class_name, instance_id = key.split('.')
            if class_name == line_name and instance_id == line_id:
                print(new_vars[class_name][instance_id])
    
    def do_delete(self, line_name, line_id):
            if not line_name:
                 print("** class name missing **")
            elif line_name != "BaseModel":
                 print("** class doesn't exist **")
            elif not line_id:
                 print("** instance id missing **")
            # elif
    
    def do_all(self, line_name):
         if nt
    
    def do_update(self, line_name, line_id):
            pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
