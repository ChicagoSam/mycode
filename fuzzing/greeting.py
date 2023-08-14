#!/usr/bin/python3
"""Python Script for Fuzz Testing"""

def get_name():
    while True:
        name = input("What is your name?")
        if name.strip():  # Check if the stripped version of the name is not empty
            return name
        else:
            print("Please enter your name.")
            # remark out above line and and enter a "default name"?
            # return "default_name"

def get_age():
    return int(input("What is your age?"))

def process_name_age(name, age):
    if age > 0 and age < 110:
        return f"Hello, {name}. Your age is verified."
    else:
        return f"I'm sorry, {name}, but I cannot verify that age."

def main():
    print(process_name_age(get_name(),get_age()))

if __name__ == "__main__":
    main()

