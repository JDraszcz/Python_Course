#------------------------------------------------------#
#                       Rectangle                      #
#------------------------------------------------------#

# In this program, like a lot of people did in Scratch we 
# are going to create inputs for rows and colums and 
# Print a rectangle

#------------------------------------------------------#
#                       Variables                      #
#------------------------------------------------------#

rows = int(input("How many rows do you want : "))
columns = int(input("What about the columns : "))
symbols = input("Enter the symbol you want to use :")

#------------------------------------------------------#
#                   Nested Loops                       #
#------------------------------------------------------#

for i in range(rows) :
    for x in range(columns):
        print(symbols, end="")
    print()