import math

#-----------------------------------------------#
#               Circumference                   #
#-----------------------------------------------#

# The formula is C = 2 pi r

# Let's ask for the radius

radius = float(input("Set the radius of the circle :"))

# Now let's calculate

circumference = 2 * math.pi * radius

print(f"The Circumference of your circle is {round(circumference, 2)}cm")

# We round the result with 2 decimals to be precise