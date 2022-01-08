#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if ord(chr(i)) != ord('q') and ord(chr(i)) != ord('e'):
        print("{}".format(chr(i)), end="")
