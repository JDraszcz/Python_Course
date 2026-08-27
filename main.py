
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

# while True : 
#     rate = float(input("Enter a value : "))
#     if rate < 0:
#         print("Impossible")
#     else:
#         break

# In this case, while rate in inferior to 0 you will have to enter a new value
# Those loops needs a break if you don´t want them to run for eternity


#---------------------------------------------------------------#
#                           For Loops                           #
#---------------------------------------------------------------#

# Once again this loop will execute a block of code
# Since the second number is exclusive
# Let's try to create a counter from 1 to 10

# for i in range(10, 0, -1):
#     print(f"Number : {i}")


# Like the String Indexation you can add a step
# In this case we've created a countdown from 10 to 1
# In our case you can also use reverse(range(1, 11))

# You can also use the number of elements in a string

# my_string = "Hi everyone !"

# for i in my_string:
#     print(i)

# In this case all the characters had been seperated

# 2 important elements in loops : continue and break
# Continue is mostly use to skip iterations
# If we wanted to modify our last example with continue

# for i in my_string :
#     if i == " ":
#         continue
#     else :
#         print(i)

# In this case all spaces will be removed

# Break will exit the loop
# In the code above only "Hi" will be printed

# If you need to print everything in one line you can do
# like the example below

# for i in range(1, 11) :
#     print(i, end=" ")

# In this case all the value are printed on the same line with a space

#---------------------------------------------------------------#
#                           Lists                               #
#---------------------------------------------------------------#


# In python there are 3 different kinds of collection :
# You can acces the datas as we did in the previous parts

# 1. Lists with [] : ordered and changeable
# 2. Set with {} : unordered and immutable (can't be modified)
# 3. Tuple with () : odered and unchangeable

# Different examples
# Lists
# countries = ["France", "Great Britain", "Russia", "Belgium"]
# print(countries[0])
# print(countries[0 : 2]) will print the first 2 countries
# As the indexation starts at 0 France is printed, 1 is Great Britain, etc
# If you need complementary abilities just print dir(countries) or help(countries)
# You can also look for an element in the list creating a boolean
# print("Banana" in countries)
# Since banana is not is the list it will be False
# If you want to modify a value :
# countries[0] = "Canada"
# In this case France will be replaced by Canada
# If you want to add an element to the end of the list use the append method
# If you want it to be to a specific index here's an example
# countries.insert(2, "Mexico")
# If you had to find the index of the element just type index and the value
# To delete the list just type countries.clear()

# Sets
# Let's create the same list as a set
# countries = {"France", "Great Britain", "Russia", "Belgium"}
# Since sets are unordered you can't find an element using a ID

# Tuples
# To make it easy it is a ordered list that you can't change
# You can have many iterances of one item bu when you create it
# you can't change the tuple anymore


#---------------------------------------------------------------#
#                       2D Collection                           #
#---------------------------------------------------------------#

# 2D collection is a list containing lists like this example below
# test = [[0, 2], [3, 8]]
# test.append([3, 6])
# print(test)

# Those collections can do everything the same than 1D collections
# If you want to access a specific item you can do this
# test[1][0] = 5
# This line replaces the 3 of the second element by 5

# If you want to print every element 1 by 1 you will need a nested loop

# for i in test :
#     for x in i:
#         print(x)

# You can also use tuples and sets and put different kinds
# Example with a numpad

# num_pad = [["1", "2", "3"], ["4", "5", "6"], ["*", "0", "#"]]

# for rows in num_pad:
#     for i in rows:
#         print(i, end="  ")
#     print()

#---------------------------------------------------------------#
#                       Dictionnaries                           #
#---------------------------------------------------------------#

# It is a collection of key and values registered like this
# {key:value}
# As always you can print dir() or help() for all the commands
# Here's an example

capitals = {"France" : "Paris" ,
            "Canada" : "Ottawa" ,
            "Australia" : "Canberra"}

# Above we have declared 3 different cities that we can print like this
# print(capitals.get("France"))
# You can use if / else to check if an item is in the dictionnary
# if capitals.get("France") :
#     print(f"The capital city is {capitals.get("France")}")
# else :
#     print("We don't have this capital city ")

# If you want to add or modify an item you can use the update function
# capitals.update({"Bulgaria" : "Sofia"})
# If you want to suppress an item
# capitals.pop("Bulgaria")
# You can also delete the latest item by using
# capitals.popitem()

# Since Sofia is referenced by Bulgaria, removing Bulgaria will also remove Sofia

# If you only need the keys of your dictionnary
# print(capitals.keys())
# On the contrary if you only want the values
# print(capitals.values())

#---------------------------------------------------------------#
#                         Random                                #
#---------------------------------------------------------------#

# If you need to create random numbers you can
import random
# And if you need help just print it
# To explain this we are goign to create a guess the number from
# 1 to 10

# number = random.randint(1, 10)

# while True :
#     guess = int(input("Try to guess the number (1 to 10 ) : "))
#     if guess == number :
#         print("You got it right")
#         break
#     else :
#         print("Try again")

# If you want a random float just use the .random()

# trying = ["test1", "test2"]

# print(random.choice(trying))

#---------------------------------------------------------------#
#                         Functions                             #
#---------------------------------------------------------------#

# Functions can be used any time you need to reitarate a set of instructions
# Here's a litte example of how to define a function and call it
# We are going to create a function that will choose a random number and print it 
# 3 times

# def example():
#     for i in range(3):
#         number = random.randint(1, 20)
#         print(number)

# example()

# In this example it can seem useless but we can use a function a lot of time and add
# some arguments to customize a message
# if you want to create a welcoming message

# def welcome(name):
#     print(f"Welcome {name} !")

# welcome("Joe")

# When we use the function we set the value name to Joe, creating the message
# PS : You can send more than one argument for a function

# You can use a return statement to stop a function and return a value

# def add(x, y):
#     z = x + y
#     return z

# print(add(1, 4))

# You can also create default arguments for the elements that are supposed to be
# often the same

# def price(initial_price, discount=0):
#     return initial_price * (1-discount)

# print(price(200))
# print(price(200, 0.3))

# The first example is still 200 but the other one prints 140

#---------------------------------------------------------------#
#                       Keywords arguments                      #
#---------------------------------------------------------------#

# In order to increase readibility you can use keywords

# def name(first, last):
#     print(f"Hello {first} {last}")

# name(last="Doe", first="John")

# other examples exists such as the end keyword or sep to separate

#---------------------------------------------------------------#
#                      *args and *kwargs                        #
#---------------------------------------------------------------#

# Don't know how to explain but here's an example of *args

# def add(*values):
#     total = 0
#     for arg in values:
#         total += arg
#     return total

# print(add(1,4,5,6))

# This example is easy to explain, you can add as many arguments as you want

# ** allows you to create the same thing with keywords, creating a dictionnary

# def indentity_card(**infos):
#     print(type(infos))
#     for key, value in infos.items():
#         print(f"{key} : {value}")


# indentity_card(name="John",
#                surname="Doe",
#                age = 23,)

# The function is displaying all the informations

#---------------------------------------------------------------#
#                          Iterables                            #
#---------------------------------------------------------------#

# Iterables are simply the way of going through a list of elements
# You can iterate everything
# If you want to iterate through a dictionnary pay attention to what 
# you want to print : my_dictionnary will print the key,
# my_dictionnary.values() the values and my_dictionnary.items()
# will print everything

#---------------------------------------------------------------#
#                   Membership operators                        #
#---------------------------------------------------------------#

# These are used to check of something is in or not in
# Example with a guessing a letter from a word

# secret_word = "Manganese"

# letter = input("Please enter a word from the secret word :")

# if letter in secret_word :
#     print(f"Congratulations you found the letter {letter} from the word")
# else :
#     print(f"Nice one but the letter {letter} is not part of the word")

#---------------------------------------------------------------#
#                       List Comprehension                      #
#---------------------------------------------------------------#

# This helps compacting the code
# We are going to print the same thing the normal way
# Then using list comprehension

# 1st method
# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
# print(doubles)

# This is the basic way, let's compact the code 

# doubles = [x *2 for x in range(1,11)]
# print(doubles)

# Here's an example with a condition

# numbers = [1, 4, 12, -8, 6, -87, -9, 4]
# positive_numbers = [num for num in numbers if num > 0]

# print(positive_numbers)

#---------------------------------------------------------------#
#                   Match-Case Statements                       #
#---------------------------------------------------------------#

# Imagine you want to create a message printing the corresponding
# day. Here's the easiest way

# choice = input("Please choose a day of the week (1-7) : ")

# try: 
#     choice = int(choice)
# except ValueError:
#     print("Please choose a valid value.")



# if choice == 1: 
#     print(f"The day number {choice} is monday")
# elif choice == 2:
#     print(f"The day number {choice} is Tuesday")
# elif choice == 3:
#     print(f"The day number {choice} is Wednesday")
# elif choice == 4:
#     print(f"The day number {choice} is Thursday")
# elif choice == 5:
#     print(f"The day number {choice} is Friday")
# elif choice == 6:
#     print(f"The day number {choice} is Saturday")
# elif choice == 7:
#     print(f"The day number {choice} is Sunday")
# else:
#     print(f"The Value {choice} is not between 1 and 7.")

# And here's how to do it using match case statement

# def day():
#     user = int(input("Please choose a number of the day (1-7) : "))

#     match user:
#         case 1:
#             print(f"The day number {user} is Monday")
#         case 2:
#             print(f"The day number {user} is Tuesday")
#         case 3:
#             print(f"The day number {user} is Wednesday")
#         case 4:
#             print(f"The day number {user} is Thursday")
#         case 5:
#             print(f"The day number {user} is Friday")
#         case 6:
#             print(f"The day number {user} is Saturday")
#         case 7:
#             print(f"The day number {user} is Sunday")
#         case _:
#             print(f"The value is incorrect")


#---------------------------------------------------------------#
#                         Modules                               #
#---------------------------------------------------------------#

# A module is a file containing code such as functions
# One of the most used is the math module
# Here's how to see every pre-existing modules

# print(help("modules"))

# Here's 3 ways to import and the differences

# import math 
# This way you will have access to everything from the module

# import math as m 
# This one gives a nickname when you have to use it

# from math import pi
# Using this you will import only the necessary and you do no longer
# have to write math.pi just write pi

# Finally you can create you own modules 
# For example you can create a python file with every functions you need


#---------------------------------------------------------------#
#                       Scope Resolution                        #
#---------------------------------------------------------------#

# This is the term used to define where a variable is visible
# LEGB rule = Local ; Enclosed ; Global ; Built-in

# Local
# Those variables are only visible where they are defined

# def num(): 
#     x = 3
#     print(x)

# print(x)

# In this example, x is not visible outside of the function
# In this way, the second print will not work

# Enclosed

# def func1():
#     x = 1
#     def func2():
#         x = 3
#         print(x)
#     func2()

# Enclosed variables are those in the parent function 
# In this example x = 1

# Global
# Those are every variables outside of every function or
# anything else

# Built-in
# Finally, built in functions are those built in modules

#---------------------------------------------------------------#
#                    If __name__ = "__main__"                   #
#---------------------------------------------------------------#

# This if statement let a code be executed only if the code is executed
# directly by the primary file
# Take a look at the banking program to see how this works