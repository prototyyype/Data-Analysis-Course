# Enter you module contents here
"""The module contains two functions: hypotenuse and area."""
import math

__version__ = "1.3"
__author__ = "prototyyype"

def hypotenuse(a, b):
    """the hypotenuse function returns the length of the hypotenuse when given
    the lengths of two other sides of a right-angled triangle"""
    return math.sqrt(a*a + b*b)

def area(a, b):
    """the area function returns the area of the right-angled triangle, when two sides,
    perpendicular to each other, are given as parameters."""
    return 0.5*a*b
