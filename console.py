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

        Usage: create <CLASS NAME> <CLASS ID>
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        This command is used to show all the data that is involved
        with the <Class name> and the <Class ID> number.

        It takes in One parameter and then splits it, after splitting
        it pass the first part to the <class_name> and the second as
        the <class_id>

        Then it checks if the <class name> is recognized by the console
        if it is and also the <class id> is in the imported file then it
        it prints it in a string representation.

        Usage: show <CLASS NAME> <CLASS ID>
        """
        # split t
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        new_dict = storage.all()
        if key in new_dict.keys():
            print(new_dict[key])
        else:
            print("** no instance found **")

    def do_delete(self, line):
        """
        This command deletes the data that has been created
        based on the <class name> and <class id>.

        After deletion, when the deleted <class name> and <class id>
        an error message is displayed on the interpreter.

        Usage: delete <CLASS NAME> <CLASS ID>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        new_dict = storage.all()
        if key in new_dict.keys():
            del new_dict[key]
        else:
            print("** no instance found **")

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
