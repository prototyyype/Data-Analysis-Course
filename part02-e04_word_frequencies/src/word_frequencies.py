#!/usr/bin/env python3
'''
Create function word_frequencies that gets a filename as a parameter and returns
a dict with the word frequencies. In the dictionary the keys are the words and
the corresponding values are the number of times that word occurred in the file
specified by the function parameter. Read all the lines from the file and split
the lines into words using the split() method. Further, remove punctuation from
the ends of words using the strip("""!"#$%&'()*,-./:;?@[]_""") method call.

Test this function in the main function using the file alice.txt. In the output,
there should be a word and its count per line separated by a tab:

The     64
Project 83
Gutenberg   26
EBook   3
of      303
'''
def word_frequencies(filename):
    freq_dict = {}
    with open(filename, "r") as rf:
        for line in rf.readlines():
            for word in line.split():
                w = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                freq_dict[w] = 1 if w not in freq_dict else freq_dict[w] + 1

    return freq_dict

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
