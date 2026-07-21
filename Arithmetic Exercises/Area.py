import math

#-----------------------------------------------#
#                     Area                      #
#-----------------------------------------------#

# For this one the formula is pi r^2

# Let's ask for the radius

radius = float(input("Choose the radius of your cicle : "))

# Let's now calculate 
area = math.pi * pow(radius, 2)

print(f"The area of your circle is {round(area, 2)} cm^2")