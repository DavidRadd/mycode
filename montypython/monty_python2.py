#!/usr/bin/env python3
"""Amazon Business & Tech | dradabau
   Conditionals - Life of Brian guessing game using a while True loop."""


roundd = 0
answer = " "

while roundd < 3 and answer != "Brian":
    roundd += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower() == "brian": # logic to check if user gave correct answer
        print("Correct!")
        break
    elif answer.lower() == "shrubbery":
        print('You gave the super secret answer!')
        break
    elif roundd == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

