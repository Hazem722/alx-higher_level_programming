#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(str[c]) in range(ord('a'), ord('z') + 1):
            i = ord(str[c]) - 32
            print(chr(i), end="")
        else:
            print(str[c], end="")
