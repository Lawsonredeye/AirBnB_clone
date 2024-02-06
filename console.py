#!/usr/bin/python3

import cmd


class Console(cmd.Cmd):
    """
    The console which would be controlling the backend of the project.
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        specifies the end of file and terminates
        the program by inputting CTRL + D
        """
        return True

    def postloop(self):
        """
        Enters a new-line automatically if True is encountered
        """
        print("")

    def do_greet(self, name):
        """
        Welcomes the Dev into the console, if name
        is inputted it welcomes the Dev. with it's name

        Args:
            greet <name>
            greet
        """
        if name:
            print(f"hello, {name}")
        else:
            print("Hi")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        Console().onecmd(" ".join(sys.argv[1:]))
    else:
        Console().cmdloop()
