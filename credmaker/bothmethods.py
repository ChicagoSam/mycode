#!/usr/bin/env python3
"""Offer the user both manual and automated options to create these files"""

#importing modules and tools
import csv

#MANUAL METHOD
def manual():
    outFile = open("admin.rc", "a")
    osAUTH = input("What is the OS_AUTH_URL? ")
    print("export OS_AUTH_URL=" + osAUTH, file=outFile)

    print("export OS_IDENTITY_API_VERSION=3", file=outFile)

    osPROJ = input("What is the OS_PROJECT_NAME? ")
    print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

    osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
    print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

    osUSER = input("What is the OS_USERNAME? ")
    print("export OS_USERNAME=" + osUSER, file=outFile)

    osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
    print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

    osPASS = input("What is the OS_PASSWORD? ")
    print("export OS_PASSWORD=" + osPASS, file=outFile)
    outFile.close()

    print("File created!")

# AUTO METHOD
# open our csv data (we want to loop across this)
def auto():
    file=input("what is the file you/'d like to export from?")
    #need .txt checker language

    with open(f"{file}", "r") as csvfile:
        # counter to create unique file names
        i = 0
        # loop across our open file line by line
        for row in csv.reader(csvfile):
            i = i + 1 # increase i by 1 (to create unique admin.rc file names)
            filename = f"admin.rc{i}" # this f string says "fill in the value of i"

            # open a file via "with". This file will autoclose when the indentations stop
            with open(filename, "w") as rcfile:
                # use the standard library print function to print our data
                # out to the open file open rcfile (open in write mode)
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                print("export OS_USERNAME=" + row[3], file=rcfile)
                print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                print("export OS_PASSWORD=" + row[5], file=rcfile)

# all of the indentation ends, so all files are auto closed

    # display this to the screen when all of the looping is over
    print("admin.rc files created!")

#Asking user for preferred method
while True:
    print("Would you like to export info Manually or Automatically?")
    q=input("M or A (or X to exit)\n")
    q=q.lower().strip() #normalizing

    if q == "m":
        print ("You chose a MANUAL export\n")
        manual()

    elif q == "a":
        print ("You chose an AUTOMATIC export\n")
        auto()

    elif q == "x":
        print ("You chose to exit!\n")
        break

    else:
        print ("please type 'm' 'a' or 'x'") # only allow those

print("Thank you for using our unhackable service!")


