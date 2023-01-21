#!/usr/bin/env python3
'''
Write a function positive_list that gets a list of numbers as a parameter, and
returns a list with the negative numbers and zero filtered out using the filter
function.

The function call positive_list([2,-2,0,1,-7]) should return the list [2,1].
Test your function in the main function.
'''
def positive_list(L):
    return list(filter(lambda x: x > 0, L))

def main():
    assert positive_list([2,-2,0,1,-7]) == [2,1]

if __name__ == "__main__":
    main()
