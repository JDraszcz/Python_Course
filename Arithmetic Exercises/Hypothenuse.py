import math

#-----------------------------------------------#
#       Hypothenuse of a right triangle         #
#-----------------------------------------------#

# Since we all know the formula 

# Let's define a and b

a = float(input("Select the value of the first side : "))
b = float(input("Select the value of the second side : "))

# Now using the formula

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The Hypothenuse is : {c}")