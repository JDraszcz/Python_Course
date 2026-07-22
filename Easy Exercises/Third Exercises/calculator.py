#------------------------------------------------------#
#                   Calculator                         #
#------------------------------------------------------#

# This program aims to do operations between 2 numbers you've chosen

# First we are going to create the variables then all the cases to do operation


#------------------------------------------------------#
#                   Variables                          #
#------------------------------------------------------#

first_number = float(input("Insert the first Value : "))
second_number = float(input("Insert the second Value : "))

operator = input("Write down the operator you want to use ( + ; - ; * ; / ) : ")

#------------------------------------------------------#
#                   If Statements                      #
#------------------------------------------------------#

if operator == "+" :
    result = first_number + second_number
elif operator == "-" :
    result = first_number - second_number
elif operator == "*" : 
    result = first_number * second_number
elif operator == "/" : 
    if second_number == 0.0 : 
        print("You can't divide by 0")
        result = "Unable to Divide because the second number is 0"
        exit
    else :
        result = first_number / second_number
else :
    print("One of the parameter is incorrect. Try again.")

print(f"The result of your operation is {result}")