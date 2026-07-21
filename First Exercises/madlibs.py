#---------------------------------------------------------------#
#                       MadLibs Game                            #
#---------------------------------------------------------------#

# The game is filling the blanks
# PN I will firstly try to do it myself then we'll see how he does it

#---------------------------------------------------------------#
#                           Idea                                #
#---------------------------------------------------------------#

# First I will write a story one
# Then ask the user a word for each blank
# Then write it again with the words the user used

story = f"Once upon a ____, living in the forest of ________ I was _______ by the Chancelor"

print("---------------------------------------------------------------")
print("         Fill the blanks in the following sentence             ")
print("---------------------------------------------------------------")
print(" ")
print(" ")
print(" ")
print(story)
print(" ")
print(" ")
print(" ")
choice_1 = input("Choose the first word    ")
print(" ")
print(" ")
print(" ")
choice_2 = input("Choose the second word   ")
print(" ")
print(" ")
print(" ")
choice_3 = input("Choose the third word    ")
print(" ")
print(" ")
print(" ")
story = f"Once upon a {choice_1}, living in the forest of {choice_2} I was {choice_3} by the Chancelor"
print(story)