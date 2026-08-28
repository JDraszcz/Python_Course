# This program has been made using the video python course 12 hours by Bro Code
import random
import string

# Let's create a variable in which we got every possible characters 
characters_available = " " + string.digits + string.punctuation + string.ascii_letters

# Let's transform it into a list to use them one by one
characters_available = list(characters_available)

# Then let's create a encryption variable with every possible characters 
# But this time we are going to shuffle them

encryption_characters = characters_available.copy()

# To shuffle the list we are using the random module

random.shuffle(encryption_characters)


# We are now going to ask the user to write a sentence to be encrypted

# encryption = input("May enter the sentence you want to encrypt : ")

# Let's create a string variable to host the result

# encrypted = ""

# Then we are using a for loop to encrypt each character

#for letter in encryption : 
    # First we search the index of the letter we are on
    # index = characters_available.index(letter)
    # We did have create a list for the encrypted characters are we
    # are looking of the corresponding character
    # encrypted += encryption_characters[index]


# print(encrypted)

# Encryption works, let's now decipher it 

# decipher = input("Enter the encrypted message : ")

# plain_message = ""

# for letter in decipher : 
#     index = encryption_characters.index(letter)
#     plain_message += characters_available[index]

# print(plain_message)

# The deciphering part is quite useless since the encryption key change 
# at every start 

# Maybe some improvement can be made 