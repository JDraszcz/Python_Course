#---------------------------------------------------------------------#
#                           Guessing Game                             #
#---------------------------------------------------------------------#

# A fully working guessing game from 1 to 100 
# Giving informations if the guess is too high or not
# Giving the number of guesses

import random

#---------------------------------------------------------------------#
#                           Code                                      #
#---------------------------------------------------------------------#

answer = random.randint(1, 100)

guesses = 0

while True :
    guess = int(input("What is your guess (1 to 100) : "))
    if guess < 1 or guess > 100:
        print("Please pick a number from 1 to 100")
    elif guess < answer:
        print("A little too low try again.")
        guesses += 1
    elif guess > answer:
        print("A little too high try again.")
        guesses+=1
    else:
        print(f"{guess} is the correct number !")
        break

print(f"Number of guesses : {guesses}")