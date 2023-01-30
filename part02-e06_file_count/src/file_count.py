#!/usr/bin/env python3
'''
Part 1.

Create a function file_count that gets a filename as parameter and returns a
triple of numbers. The function should read the file, count the number of lines,
words, and characters in the file, and return a triple with these count in this
order. You get division into words by splitting at whitespace. You don't have to
remove punctuation.

Part 2.

Create a main function that in a loop calls file_count using each filename in
the list of command line parameters sys.argv[1:] as a parameter, in turn. For
call python3 src/file_count file1 file2 ... the output should be

?      ?       ?       file1
?      ?       ?       file2
...
The fields are separated by tabs (\t). The fields are in order: linecount,
wordcount, charactercount, filename.
'''

import sys

def file_count(filename):
    line_count, word_count, char_count = 0,0,0

    with open(filename, "r") as rf:
        while (line := rf.readline()):
            line_count += 1
            char_count += len(line)
            word_count += len(line.split())

    return (line_count, word_count, char_count)

def main():
    if len(sys.argv) > 1:
        for example_file in sys.argv[1:]:
            print('{}\t{}\t{}\t{}'.format(*file_count(example_file), example_file))

if __name__ == "__main__":
    main()
