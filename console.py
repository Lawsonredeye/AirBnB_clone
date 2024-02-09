#!/usr/bin/python3
"""
The console wich controls the entire C.R.U.D process
"""
import cmd


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
