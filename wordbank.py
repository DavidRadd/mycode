#!/usr/bin/env python3
""" Amazon Business & Tech | Dradabau"""
import random

wordbank= ["indentation", "spaces"] 
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric",
        "Chris", "Cory", "Ebrima", "Franco",
        "Greg", "Hoon", "Joey", "Jordan",
        "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)
print (wordbank)

num= int(input("Enter a number 1-18: "))
student_name = tlgstudents[num]

print(student_name)

print("Random name: " + random.choice(tlgstudents))

print (random.random())

def myfunc():
    return .12

#print(random.shuffle(wordbank, myfunc))

print(wordbank)
print(random.shuffle(tlgstudents))
random.shuffle(wordbank, myfunc)
print(wordbank)
