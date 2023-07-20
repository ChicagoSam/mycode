#! /usr/bin/env python3

def nameday():
    uname = input("What is your name? ")
    dname = input("What day of the week is it? ")

    print("Hello,", end=" ")
    print(uname, end="")
    print("!", end=" ")
    print("Happy", end=" ")
    print(dname, end="")
    print("!")

nameday()
