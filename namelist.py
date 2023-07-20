#!/usr/bin/env python3

wordbank= ["indentation", "spaces"]

tlgstudents= ['Alex', 'Benji', 'Cayla', 'Demetra', 'Derek', 'Deshawn', 'James', 'Maria', 'Marylyn', 'Nor', 'Sal', 'Sammy']

wordbank.append(4)

while True:
    num=int(input("Can I have a number between 1 and 12?\n>")) - 1
    if 0 <= num <=11:
        break
    print("Please select a valid number!\n")

name=tlgstudents[num]

print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent")

