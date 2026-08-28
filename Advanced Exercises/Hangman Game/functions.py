# This file hosts everything needed to play the game
# In order to choose a word to find we need the 
# random module
import sys
import random

# First we are going to need a list of possible words
possible_words = ("Watermelon", "Containment", "Fulfillment", "Cherry", "Bell")

# Let's now create the hangman using ASCII-art

hangman_poses = {
                 0: ("   \n"
                     "   \n"
                     "   "),

                 1: (" O \n"
                     "   \n"
                     "   "),

                 2: (" O \n"
                     " | \n"
                     "   "),

                 3: (" O \n"
                     " | \n"
                     "/  "),

                 4: (" O  \n"
                     " |  \n"
                     "/ \\"),


                 5: (" O  \n"
                     "/|  \n"
                     "/ \\"),


                 6: (" O  \n"
                     "/|\\\n"
                     "/ \\")

                                }


# Let's now create the functions we will need 


def display_man(wrong):
    for line in hangman_poses[wrong]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer): 
    print(" ".join(answer))


def main(): 
    answer = random.choice(possible_words)
    wrong = 0
    hint = ["_"] * len(answer)
    guessed = set()
    is_running = True

    while is_running : 
        display_man(wrong) 
        display_hint(hint)

        guess = input("May enter a letter : ").lower()

        # We check that only one valable character had been entered

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed:
            print(f"The letter {guess} is already guessed !")
            continue

        guessed.add(guess)


        # Let's now verify if a letter is in the word
        if guess in answer:
            for i in range(len(answer)): 
                if answer[i] == guess:
                    hint[i] = guess

        else: 
            print(f"The letter {guess} is not in the word")
            wrong += 1














if __name__ == "__main__" :
    print("You are not allowed to execute the code from here") 
    sys.exit()