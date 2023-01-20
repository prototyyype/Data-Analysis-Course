#!/usr/bin/env python3
'''
Write a function transform that gets two strings as parameters and returns a
list of integers. The function should split the strings into words, and convert
these words to integers. This should give two lists of integers. Then the
function should return a list whose elements are multiplication of two integers
in the respective positions in the lists. For example transform("1 5 3", "2 6 -1")
should return the list of integers [2, 30, -3].

You have to use split, map, and zip functions/methods. You may assume that the
two input strings are in correct format.
'''

def transform(s1, s2):
    l1 = [int(n) for n in s1.split(" ") if len(s1) > 0]
    l2 = [int(n) for n in s2.split(" ") if len(s2) > 0]

    return list(map(lambda x: x[0]*x[1], zip(l1, l2)))

def main():
    assert transform("1 5 3", "2 6 -1") == [2, 30, -3]
    assert transform("7 4 -8", "4 -9 2") == [28, -36, -16]
    assert transform("", "") == []

if __name__ == "__main__":
    main()
