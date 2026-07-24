#---------------------------------------------------#
#                       RPS                         #
#---------------------------------------------------#

# We are going to create the list of possibilities
# Then the random function will choose 

#---------------------------------------------------#
#                       Code                        #
#---------------------------------------------------#


import random

possibilities = ("rock", "paper", "scissors")
your_points = 0
opponent_points = 0
is_running = True

print("------------------------------------------------------------")
print("           Rock         Papers       Scissors               ")
print("------------------------------------------------------------")

print("Round of 3")
print("Choose between those possibilites :")

for possibility in possibilities :
    print(possibility)


while is_running == True : 
    guess = input("Choose your weapon : ").lower()
    opponent = random.choice(possibilities)
    if guess != "rock" and guess != "paper" and guess != "scissors" :
        print("You must choose one of those")
    else:
        if guess == "rock":
            if opponent == "scissors":
                print("You won !")
                your_points += 1
            elif opponent == "rock":
                print("Draw")
            else:
                print("You lose...")
                opponent_points+=1
        elif guess == "paper":
            if opponent == "rock":
                print("You won !")
                your_points += 1
            elif opponent == "paper":
                print("Draw")
            else:
                print("You lose...")
                opponent_points+=1
        else :
            if opponent == "paper":
                print("You won !")
                your_points += 1
            elif opponent == "scissors":
                print("Draw")
            else:
                print("You lose...")
                opponent_points+=1

    if opponent_points == 3 or your_points == 3 :
        print("Game is over")
        print(f"Oppenent Score = {opponent_points}")
        print(f"Your Score : {your_points}")
        if your_points > opponent_points:
            print("You Won ! Congratulations")
        else:
            print("Nice Play ! Let's try again")
        is_running = False

print("End of the loop")
            
