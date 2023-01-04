#!/usr/bin/env python3

import math

def areaTriangle(b,h):
    return b*h*.5
def areaRectangle(w,h):
    return w*h
def areaCircle(r):
    return r*r*math.pi
def main():
    # enter you solution here
    userShape = input("Choose a shape (triangle, rectangle, circle):")

    while userShape != "":
        if userShape == "triangle":
            b = int(input("Give base of the triangle: "))
            h = int(input("Give height of the triangle: "))
            print("The area is {:.6f}".format(areaTriangle(b,h)))

        elif userShape == "rectangle":
            w = int(input("Give width of the rectangle: "))
            h = int(input("Give height of the rectangle: "))
            print("The area is {:.6f}".format(areaRectangle(w,h)))

        elif userShape == "circle":
            r = int(input("Give radius of the circle: "))
            print("The area is {:.6f}".format(areaCircle(r)))

        else:
            print("Unknown shape!")

        userShape = input("Choose a shape (triangle, rectangle, circle):")


if __name__ == "__main__":
    main()
