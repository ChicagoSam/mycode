#!/usr/bin/env python3

hellenkeller= {
"Occupation"  : "Author, political, activist, lecturer",
"Education"   : "Radcliffe College",
"Powers"      : "Heightened sense of smell",
"Vertical"    : "44.5",
"Mile time"   : "4:42"
}

hellenkeller["Bench press"]= "375"

print(hellenkeller.keys())

fact= input("Choose one of the facts above\n>")

# if the KEY is in the dict THEN
print( hellenkeller.get(fact, "Please choose one of the above facts!") )

print(f"Hellen Keller's {fact} is {hellenkeller[fact]}")
