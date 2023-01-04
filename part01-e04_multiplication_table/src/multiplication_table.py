#!/usr/bin/env python3


def main():
    for i in range (1,11):
        for j in range(1,11):
            print('{:4d}'.format(j*i), end="")
        print('\n', end="")
if __name__ == "__main__":
    main()
