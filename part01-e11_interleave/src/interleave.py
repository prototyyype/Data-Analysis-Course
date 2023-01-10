#!/usr/bin/env python3

def interleave(*lists):
    new_list = []
    x = list(zip(lists))

    for row in range(len(x[0][0])):
        for col in range(len(x)):
            new_list.append(x[col][0][row])

    return new_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
