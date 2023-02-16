#!/usr/bin/env python3

class Prepend(object):
    """Documentation string of the class"""

    def __init__(self, param1):
        """This initialises an instance of type Prepend"""
        self.text = param1

    def write(self, prepend):
        print(self.text + prepend)

def main():
    p = Prepend("+++ ")
    p.write("Hello");

if __name__ == "__main__":
    main()
