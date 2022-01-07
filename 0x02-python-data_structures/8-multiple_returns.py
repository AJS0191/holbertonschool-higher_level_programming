#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        imatuple = len(sentence), sentence[0]
    else:
        imatuple = 0, None
    return imatuple
