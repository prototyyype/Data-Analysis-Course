#!/usr/bin/env python3
import re
'''
Write function integers_in_brackets that finds from a given string all integers
 that are enclosed in brackets.

Example run: integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")
returns [12, -43, 12]. So there can be whitespace between the number and the
brackets, but no other character besides those that make up the integer.

Test your function from the main function.
'''

def integers_in_brackets(s):
    # only in brackets and stand alone
    pattern = r'\[\s*([+-]?\d+)\s*\]'
    return [int(a) for a in re.findall(pattern, s)]

def main():
    assert (
        integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")
    ) == [12, -43, 12]

if __name__ == "__main__":
    main()
