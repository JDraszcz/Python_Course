
#---------------------------------------------------------------#
#   Never be that good in Python I'll try to improve myself     #
#  The beginnings I'll do there is made with the following video#
#      https://www.youtube.com/watch?v=ix9cRaBkVe0              #
#---------------------------------------------------------------#

#---------------------------------------------------------------#
#           PN means personnal note, not useful                 #
#---------------------------------------------------------------#


#---------------------------------------------------------------#
#                           Variables                           #
#---------------------------------------------------------------#

first_kind_of_variable = "My Princess"   # This is a string
second_kind_of_variable = 13             # This is a integer
third_kind_of_variable = 10.05           # This is a floating value
fourth_kind_of_variable = True           # This is a boolean

#---------------------------------------------------------------#
#                 Basic Printing Statements                     #
#---------------------------------------------------------------#

# How to simply print a string which is not a variable
# print("Here's my string !")

# If you want to print a variable
# print(my_variable)

# If you want to print both in one print statement 2 options
# print("My string is ", my_variable)
# Otherwise you can make a f-string
# print(f"My String is {my_variable}")



#---------------------------------------------------------------#
#                         Typecasting                           #
#---------------------------------------------------------------#

# Typecasting is the process of converting a variable type to another

# PN : Maybe what we use while doing an input ? 

# There are 4 types, representing the types of variables
# str() int() float() and bool()

# How does it work ? 
# Using the variable "second_kind_of_variable" we'll transform an integer
# To a String and the output will be the type

# First let's check the type of the function at the beginning

# print(type(second_kind_of_variable)) 
# Prints int as intended 

# Let's now modify the type to a string
#changing_type = str(second_kind_of_variable)

# Then check that the output is indeed a string
# print(type(changing_type)) 
# Prints str for string

# Notice that if your changing a floating value for an integer 
# Decimals will be suppressed
# For exemple 3.25 will become 3 
# On the contrary if an integer becomes a floating value 
# A decimal will appear
# If the integer is 13 it will be 13.0

 

# For the boolean, if the value is null it will print False
# Otherwise it will be true

#---------------------------------------------------------------#
#                           Inputs                              #
#---------------------------------------------------------------#

# When you want to give the choice to the user, you have to create an imput
# Here's a simple way to ask the user's name
# user_name = input("What's your name ?")
# This give an input to the user to write down his name
# The value of the variable will now be the user's name
# print(f"Nice to meet you {user_name}")
# That's how you can easily make a welcoming message

# However inputs basically returns string
# If you want to change the data type you have to specify it
# For example, if you want the user's age
# user_age = int(input("How old are you ?"))
# And then you can just use it or do math with it ! 
# print(f"You're {user_age} years old !")
# user_double = user_age * 2 
# print(f"The double of your age is {user_double}")


#---------------------------------------------------------------#
#                      Arithmetics                              #
#---------------------------------------------------------------#

# Here's the list of the operator, used in float and integer
# Let's say we have an integer variable set to 1 called number
# number = 1.25
# number += 1   This one add 1 to number
# number -= 1   This one substract 1 to number
# number *= 2   This one doubles the variable
# number **= 2  This one squares the number
# number /= 2   This one divides to variable by 2
# number %= 1   Modulo gives the remainder when one number is divided by another. 

# Some other basics, keeping our variable number but using another one called result
# result = round(number, 1)   Will round number and the output will be 1 and 1 decimal
# result = abs(number)     Always give the positive one 
# result = pow(number, 3)  This one will power number by 3 

# To compare different values you can you these
# result = max(a, b, c) will give the maximum as the output
# result = min(a, b, c) will give the mininun as the output
# 
# Otherwise if you need more arithmetics tools you can use the import math 
# 
# Then you can use many features such as math.pi, giving exactly pi
# You can have the exponential, the square root, the power, etc
# The function ceil round the numbers to the upper rounded one
# The contrary is floor, which will round the the lower one


#---------------------------------------------------------------#
#                           If Statements                       #
#---------------------------------------------------------------#

# If you want something to happen if the requirement is met you can use 
# An if statement
# If you want to print "Well Play if user's score is greater than 80"
# user_score = float(input("Type your score : "))

# if user_score > 80: 
#    print("Well Play !")
# !!! Indentation is VERY important !!!

# If you now want to print another message if the requirement is not met

# if user_score > 80: 
#     print("Well Play !")
# else : 
#     print(f"Nice try but your score is only {user_score} points.")

# If you need to check other statements you can add an elif statement like this

# if user_score > 80 :
#     print("Well Play !")
# elif user_score >= 60 :
#     print("Nice One !")
# else :
#     print(f"Nice try but you only got {user_score} points.")

# If you want to check if a variable is equal to a value use ==

#---------------------------------------------------------------#
#                      Logical Operators                        #
#---------------------------------------------------------------#

# 3 Basics Logical Operators

# or : 1 of the conditions must be true

# and : All of the requirements has to be met

# not : The condition needs to be inverted 

# No need for an example except for the NOT
# Let's do a age verification 

# user_age = int(input("Insert your Age : "))

# if user_age > 0 and user_age <= 110 :
#     if user_age < 18:
#         is_minor = True
#     else :
#         is_minor = False
    
# else :
#    print(f"You can't have {user_age} years old")

# if not is_minor :
#     print("You're major, at least 18 years old")
# else :
#     print("You're still a minor")

# The Code is not perfect but not is_minor is going to check if it is set to False 

#---------------------------------------------------------------#
#                   Conditionnal Expressions                    #
#---------------------------------------------------------------#


# You can have an if / else statement directly in one line in a print for example
# A little example with the age once again

# age = int(input("May enter your age : "))

# print("You're major" if age >= 18 else "You're a minor")

#---------------------------------------------------------------#
#                       String Methods                          #
#---------------------------------------------------------------#

# Here's a few list of the most important things you can do on a string
# let's call our variable string and it's data type string

# 1. len(string)                       => Give the length of the string
# 2. string.find("x")                  => Looking for the first x in the String
# 3. string.rfind("x")                 => Looking for the last iterance
# 4. string.capitalize()               => Capitalize the first item
# 5. string.upper()                    => Put Uppercase to all letters
# 6. string.lower()                    => Put lowercase to all letters
# 7. string.isdigit()                  => Boolean true if all elements are digits
# 8. string.isalpha()                  => Boolean true if all elements are alphabetical
# 9. string.count("x")                 => Count the number of x in the string
# 10. string.replace("x", "z")         => Replace all x with z

# If you need more just type print(help(str))

#---------------------------------------------------------------#
#                    String Indexation                          #
#---------------------------------------------------------------#

# Indexing means accessing a specific part
# You need to use squared brackets
# Here's how to do it and an example
# [beginning of the index : end : steps]
# ! The end index is excluded ! 
# Let's explain it with an example
# Let's write a string then print the result of an indexation
# string = "My super string so fun to use !"
# indexation = string[3 : 20 : 3]

# print(indexation)
# In this example we are taking all characters from super to the u of fun
# and we are doing 3 steps by 3 steps so the first one is s
# then e, s, i, space, space and then we are out of reach
# The result will be sesi 
# You can also take the last index elements by using negative numbers
# In our example, string[-1] will print the !

#---------------------------------------------------------------#
#                       Format Specifiers                       #
#---------------------------------------------------------------#

# Quite hard to explain, just remember that you can layout your values
# To do this, just add the so-called flags when asking a varible
# print(f"Take a look at my variable {variable:flags}")
# There are a tons of flags but some can be very useful for app banks for example
# Here's an example

# bank_account = 2548.32
# next_withdrawal = -658.24
# future_ammount = bank_account + next_withdrawal

# print(f"Your bank account has for now an ammount of ${bank_account:+,.1f}")
# print(f"However a withdrawal of {next_withdrawal:+,.1f} is now scheduled")
# print(f"Your future ammount will be : ${future_ammount:<10.1f}")
# You can now see on the first print that we print a positive sign if the value is
# We also add a comma automatically
# Then we ask for 1 decimal
# It's the same on the second except that a negative value a - will be printed
# Last the third print lets 10 characters maximums, put the value to the left with <
# and decimal

#---------------------------------------------------------------#
#                        While loops                            #
#---------------------------------------------------------------#   

# It's basically a loop that repeat an action while a condition is true

# Easy example

# password = "1234"
# password_check = input("May enter the password : ")

# while password_check != password :
#     print("Incorrect password")
#     password_check = input("May enter the password")
# else :
#     print("Welcome admin !")

# While the password typed is different you will have to type it again and again

# You can also create this kind of while loops

while True : 
    rate = float(input("Enter a value : "))
    if rate < 0:
        print("Impossible")
    else:
        break
