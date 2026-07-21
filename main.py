
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
