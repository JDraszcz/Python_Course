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
           1 : "⚀",
           2 : "⚁",
           3 : "⚂",
           4 : "⚃",
           5 : "⚄",
           6 : "⚅"
         }


dice = []
total = 0
ask = int(input("How many dices do you want ?"))
if ask > 0: 
    for die in range(ask) :
        new = random.randint(1, 6)
        dice.append(new)
        total += new
print(dice)
print("--------------------------------")
for die in dice : 
    print(values.get(die))
        

