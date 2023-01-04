#!/usr/bin/env python3
def triple(n):
    return n*3
def square(n):
    return n*n

def main():
    for i in range(1,11):
        t, s = triple(i), square(i)
        if s > t:
            break
        print("triple({})=={} square({})=={}".format(i,t,i,s))


if __name__ == "__main__":
    main()
