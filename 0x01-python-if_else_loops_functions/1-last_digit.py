#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = number % 10
strF = "Last digit of {} ".format(number)
strG = "and is greater than 5"
strL = "and is less than 6 and not 0"
str0 = "and is 0"

strIs = "is {} ".format(lastD)
if number < 0:
    lastD = (number * -1) % 10
    strIs = "is {} ".format(lastD * -1)

if lastD == 0:
    print("{}{}{}".format(strF, strIs, str0))
elif lastD < 6:
    print("{}{}{}".format(strF, strIs, strL))
else:
    print("{}{}{}".format(strF, strIs, strG))
