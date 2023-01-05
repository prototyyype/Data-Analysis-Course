#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    # returns solutions as a tuple
    d = b**2-(4*a*c)

    if d == 0:
        x = (-b/(2*a), -b/(2*a))
    elif d > 0:
        x = (((-b - math.sqrt(d))/(2*a)), ((-b + math.sqrt(d))/(2*a)))
    else:
        x = None

    return x

def main():
    # print(solve_quadratic(1,-3,2))
    # print(solve_quadratic(1,2,1))
    # print(solve_quadratic(1,10,-24))
    print(solve_quadratic(-2,2,1))

if __name__ == "__main__":
    main()
