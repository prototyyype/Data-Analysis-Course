#!/usr/bin/env python3
'''
Create your own module as file triangle.py in the src folder. The module should
contain two functions:

* hypotenuse: which returns the length of the hypotenuse when given the lengths of
two other sides of a right-angled triangle

* area: which returns the area of the
right-angled triangle, when two sides, perpendicular to each other, are given
as parameters.

Make sure both the functions and the module have descriptive
docstrings. Add also the __version__ and __author__ attributes to the module.
Call both your functions from the main function (which is in file usemodule.py).
'''

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    triangle.hypotenuse(3, 4) #== 5
    triangle.area(3,4) #== 6


if __name__ == "__main__":
    main()
