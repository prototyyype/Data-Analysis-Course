#!/usr/bin/env python3
'''
Part 1.
Write function file_extensions that gets as a parameter a filename. It should
read through the lines from this file. Each line contains a filename. Find the
extension for each filename. The function should return a pair, where the first
element is a list containing all filenames with no extension (with the preceding
period (.) removed). The second element of the pair is a dictionary with
extensions as keys and corresponding values are lists with filenames having that
extension.r

If the file contains the following lines:
file1.txt
mydocument.pdf
file2.txt
archive.tar.gz
test

then the return value should be the pair:
(["test"],
{ "txt" : ["file1.txt", "file2.txt"],
"pdf" : ["mydocument.pdf"],
"gz" : ["archive.tar.gz"]
} )

Part 2.

Write a main method that calls the file_extensions function with
"src/filenames.txt" as the argument. Then print the results so that for each
extension there is a line consisting of the extension and the number of files
with that extension. The first line of the output should give the number of
files without extensions.

With the example in part 1, the output should be

1 files with no extension
gz 1
pdf 1
txt 2
Had there been no filenames without extension then the first line would have
been 0 files with no extension. In the printout list the extensions in
alphabetical order.
'''
import sys

def file_extensions(filename):
    no_extension_files, extension_files = [], {}

    with open(filename, "r") as rf:
        while (line := rf.readline().strip("\n")):
            if "." not in line:
                no_extension_files.append(line)
            else:
                ext = line.rsplit(".",1)[1]
                extension_files[ext] = [line] if ext not in extension_files else sorted([line] + extension_files[ext])
    return (no_extension_files, extension_files)

def main():
    for example_file in sys.argv[1:]:
        list_result, dict_result = file_extensions(sys.argv[0])
        print(len(list_result),"files with no extension")

        num_dict = {k: len(dict_result[k]) for k in sorted(list(dict_result.keys()))}
        for ext, num_files in num_dict.items():
            print('{} {}'.format(ext, num_files))

if __name__ == "__main__":
    main()
