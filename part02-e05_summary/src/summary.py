#!/usr/bin/env python3
'''
PART ONE:
Create a function called summary that gets a filename as a parameter. The input
file should contain a floating point number on each line of the file. Make your
function read these numbers and then return a triple containing the sum, average,
and standard deviation of these numbers for the file.

The main function should call the function summary for each filename in the list
sys.argv[1:] of command line parameters. (Skip sys.argv[0] since it contains the
name of the current program.)

Example of usage from the command line: python3 src/summary.py src/example.txt src/example2.txt

Print floating point numbers using six decimals precision. The output should look like this:

File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
File: src/example2.txt Sum: 5446.200000 Average: 1815.400000 Stddev: 3124.294045

PART TWO
If some line doesn’t represent a number, you can just ignore that line. You can
achieve this with the try-except block. An example of recovering from an
exceptional situation:

try:
    x = float(line)           # The float constructor raises ValueError
    exception if conversion is no possible
except ValueError:
    # Statements in here are executed when the above conversion fails

'''

import sys
import re
import math

def summary(filename):
    num_sum, avg, dev = 0,0,0

    with open(filename, "r") as rf:
        nums = []

        for line in rf.readlines():
            try:
                nums.append(float(line.strip()))
            except ValueError:
                continue

        n = len(nums)
        num_sum = sum(nums)
        avg = num_sum/n
        dev = math.sqrt(sum([(x-avg)**2 for x in nums])/(n-1))

    return num_sum, avg, dev

def main():
    if len(sys.argv) > 1:
        for example_file in sys.argv[1:]:
            print("File: {} Sum: {:.6f} Average: {:.6f} Stddev: {:.6f}".format(example_file,*summary(example_file)))

if __name__ == "__main__":
    main()
