#!/usr/bin/env python3

# Create a function named detect_ranges that gets a list of integers as a
# parameter. The function should then sort this list, and transform the list
# into another list where pairs are used for all the detected intervals. So
# 3,4,5,6 is replaced by the pair (3,7). Numbers that are not part of any
# interval result just single numbers. The resulting list consists of these
# numbers and pairs, separated by commas. An example of how this function works:
#
# print(detect_ranges([2,5,4,8,12,6,7,10,13]))
# [2,(4,9),10,(12,14)]

def detect_ranges(L):
    # sort list
    L = sorted(L)
    print(L)
    # L = [2, 4, 5, 6, 7, 8, 10, 12, 13]

    isConsecNum = False
    curIdx = 0
    newList = []


    for i in range(len(L)-1):
        isConsecNum = (L[i+1] == L[i] + 1) # if next number is 3

        if not isConsecNum:
            newList.append(L[curIdx]) if curIdx == i else newList.append((L[curIdx], L[i]+1))
            curIdx = i+1
    print("i:",i)
    print("curIdx:", curIdx)
    
    # append either a number or a tuple
    isConsecNum = (L[i+1] == L[i] + 1) # if next number is 3

    if not isConsecNum:
        newList.append(L[curIdx]) if curIdx == i else newList.append((L[curIdx], L[i]+1))
        curIdx = i+1


    return newList

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
