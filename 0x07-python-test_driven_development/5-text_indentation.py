#!/usr/bin/python3


"""This module contains the text indentation function"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] != '.' and text[i] != '?' and text[i] != ':':
            print("{}".format(text[i]), end="")
            i = i + 1
        else:
            if (i + 2) >= len(text):
                break
            else:
                print("{}".format(text[i]), end="\n\n")
                if text[i + 1] == ' ':
                    i = i + 2
                    a = 0
                    while text[i + a] == ' ':
                        a += 1
                    i += a
                else:
                    i = i + 1
