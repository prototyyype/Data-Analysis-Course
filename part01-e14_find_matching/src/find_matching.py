#!/usr/bin/env python3
# Write function find_matching that gets a list of strings and a search string
# as parameters. The function should return the indices to those elements in the
 # input list that contain the search string. Use the function enumerate.

def find_matching(L, pattern):
    idx_match = []
    for i, wrd in enumerate(L):
        if pattern in wrd:
            idx_match.append(i)

    return idx_match

def main():
    assert (
        find_matching(["sensitive", "engine", "rubbish", "comment"], "en") == [0, 1, 3]
    )

if __name__ == "__main__":
    main()
