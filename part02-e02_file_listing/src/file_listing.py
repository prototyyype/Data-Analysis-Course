#!/usr/bin/env python3
'''
The file src/listing.txt contains a list of files with one line per file. Each
line contains seven fields: access rights, number of references, owner's name,
name of owning group, file size, date, filename. These fields are separated with
one or more spaces. Note that there may be spaces also within these seven fields.

Write function file_listing that loads the file src/listing.txt. It should
return a list of tuples (size, month, day, hour, minute, filename). Use regular
expressions to do this (either match, search, findall, or finditer method).
'''

import re

def file_listing(filename="src/listing.txt"):
    listings = []
    with open(filename, "r") as rf:
        pattern = r"(\d+)\s+([A-Za-z]+)\s+(\d+)\s+(\d+):(\d+)\s+(.*)\n"
        # for line in rf: # -rwxr-xr-x 1 jttoivon hyad-all    2356 Dec 11 11:50 add_colab_link.py
        #     # (s, mth, d, hr, min, file)
        #
        #     size, mth, day, hr, min, file_name = (re.findall(pattern, line)[0])

        return [(re.findall(pattern, line)[0]) for line in rf]

        # line = rf.readline()
        # listings.append(line)
        # while rf:
        #     line = rf.readline()
        #     listings.append(line)
        # for i in range(5):            # And read the first five lines
        #     line = rf.readline()
        #     print(line)
    # pattern = ""
    #
    #
    # return [(s, mth, d, hr, min, file) for x in re.findall(pattern, s)]

def main():
    file_listing()

if __name__ == "__main__":
    main()
