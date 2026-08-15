#----------------------------------------------------------#
#                   Rolling dices                          #
#----------------------------------------------------------#

# In this exercise we are going to create a dictionnary with 
# a value and its meaning with a dice then we will ask the user
# the number of dice he wants and we calculate the total after
# printing them

#----------------------------------------------------------#
#                   Dictionnary                            #
#----------------------------------------------------------#
import random

values = {
           1 : "1",
           2 : "2",
           3 : "3",
           4 : "4",
           5 : "5",
           6 : "6"
         }


dice = []
total = 0
ask = int(input("How many dices do you want ?"))

print(ask)

for die in range(ask) :
    dice.append(random.randint(1, 6))

print(dice)