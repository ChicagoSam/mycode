#!/usr/bin/env python3

# Oppnum is running points total that determines  % that you are Oppenheimer
oppnum= 0

# Two random lists of positive comments to keep repeat visits fresh
import random

def congrats():
    congrats = [
            "How interesting!",
            "What a lovely name!",
            "The 'J' stands for 'Juicy'--but you knew that"
            "Very impressive!",
            "You must be very important!",
            "You should be proud!",
            ]
    random_congrats2 = random.choice(congrats)
    return random_congrats2

print ("ARE **YOU** J. ROBERT OPPENHEIMER?!?")
print () # empty print() commands for formatting

# QUESTION 1
while True:
    print("Question 1: Is your name J. Robert Oppenheimer?")
    q1=input("y)es  n)o  m)aybe\n")
    q1=q1.lower().strip() # normalizing user input

    if q1 == "y":
        print(congrats())
        oppnum += 33
        break

    elif q1 == "n":
        print("That's a shame.\n")
        break

    elif q1 == "m":
        print("I forget my name sometimes too.\n")
        oppnum += 10
        break

    else:
        print("Please type 'y' 'n' or 'm'\n") # only allow y, n, m

print () # empty print() commands for formatting

# QUESTION 2
while True:
    print("Question 2: Were you in charge of the Manhattan Project?")
    q2=input("y)es  n)o  m)aybe\n")
    q2=q2.lower().strip() # normalizing user input

    if q2 == "y":
        print(congrats())
        oppnum += 33
        break

    elif q2 == "n":
        print("You should have more ambition.\n")
        break

    elif q2 == "m":
        print("You should doublecheck your planner.\n")
        oppnum += 10
        break

    else:
        print("Please type 'y' 'n' or 'm'\n") # only allow y, n, m

print() # empty print() commands for formatting


# QUESTION 3
while True:
    print("Question 3: Are you alive? Be honest!")
    q3=input("y)es  n)o  m)aybe\n")
    q3=q3.lower().strip() # normalizing user input

    if q3 == "y":
        print("You're looking good!\n")
        oppnum = 0
        break

    elif q3 == "n":
        print("My condolences.\n")
        break

    elif q3 == "m":
        print("You should make a doctor's appointment!\n")
        oppnum += 10
        break

    else:
        print("Please type 'y' 'n' or 'm'\n") # only allow y, n, m

#END OF QUIZ FOR NOW, may add more questions/adjust %

print() # empty print() commands for formatting

# RANGES FOR PLAIN LANGUAGE RESULTS
range0 = range(0, 1)
range1 = range(2, 50)
range2 = range(51, 100)

# PERCENTAGE RESULTS OF QUIZ
print(f"There is a {oppnum}% chance of you being Robert Oppenheimer.")

# PLAIN LANGUAGE RESULTS - COMPARING OPPNUM VS RANGES
while True:
    if oppnum in range0:
        print("Therefore, you are ABSOLUTELY NOT Robert Oppenheimer.")
        break

    elif oppnum in range1:
        print("So, you are PROBABLY NOT Robert Oppenheimer.")
        break

    elif oppnum in range2:
        print("You are MOST LIKELY Robert Oppenheimer.")
        break

print()
print("Thank you for taking our absolutely accurate and 100% legally binding test.")
print()
