#!/usr/bin/env python3
'''
Write a function sum_equation which takes a list of positive integers as
parameters and returns a string with an equation of the sum of the elements.

Example: sum_equation([1,5,7]) returns "1 + 5 + 7 = 13" Observe, the spaces
should be exactly as shown above. For an empty list the function should return
the string "0 = 0".
'''
def sum_equation(L):
    s = ""

    if len(L) < 2:
        return "0 = 0" if len(L) == 0 else (str(L[0])+" = "+str(L[0]))
    else:
        for num in L[:-1]:
            s += str(num) + " + "
        s += str(L[-1]) + " = " + str(sum(L))

    return s

def main():
    assert sum_equation([]) == "0 = 0"
    assert sum_equation([0]) == "0 = 0"
    assert sum_equation([12]) == "12 = 12"
    assert sum_equation([2,3]) == "2 + 3 = 5"
    assert sum_equation([1,5,7]) == "1 + 5 + 7 = 13"

if __name__ == "__main__":
    main()
