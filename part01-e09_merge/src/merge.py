#!/usr/bin/env python3
import random

def merge(L1, L2):
    a = []
    i, j = 0, 0

    # Compares the two lists by each element one by one
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            a.append(L1[i])
            i += 1
        else:
            a.append(L2[j])
            j += 1

    # Catches additional elements remaining if one list is longer than the other
    while i < len(L1):
        a.append(L1[i])
        i += 1
    while j < len(L2):
        a.append(L2[j])
        j += 1

    return a

def main():
    # l1 = [1, 4, 8, 22, 23, 35, 38, 39, 40, 49]
    # l2 = [4, 5, 6, 16, 24, 27] #, 35, 37, 41, 49]
    l1 = sorted(random.sample(range(1,50), 10))
    l2 = sorted(random.sample(range(1,50), 10))
    newList = merge(l1, l2)

    print("l1:",l1)
    print("l2:",l2)
    print("sorted list:", newList)

    assert newList == sorted(l1+l2)


if __name__ == "__main__":
    main()
