#!/usr/bin/env python3
import random
# Create a function named detect_ranges that gets a list of integers as a
# parameter. The function should then sort this list, and transform the list
# into another list where pairs are used for all the detected intervals. So
# 3,4,5,6 is replaced by the pair (3,7). Numbers that are not part of any
# interval result just single numbers. The resulting list consists of these
# numbers and pairs, separated by commas. An example of how this function works:
#
# print(detect_ranges([2,5,4,8,12,6,7,10,13]))
# [2,(4,9),10,(12,14)]
def detect_range(userList):
    # First element in the list
    start = userList[0]
    d = 1

    for elem in userList[1:]:
        # Element in row, just count up
        if elem == start + d:
            d += 1
            continue

        # Otherwise, yield
        yield start if d == 1 else (start, start+d)

        start = elem
        d = 1

    yield start if d == 1 else (start, start+d)

def detect_ranges(userList):
    L = sorted(userList)   # sort list
    return list(detect_range(L))

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    # L = random.sample(range(50), 30)
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
