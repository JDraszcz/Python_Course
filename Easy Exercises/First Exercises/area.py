#--------------------------------------#
#           Area Calculator            #
#--------------------------------------#

# The exercise aims to use inputs and arithmetics 
# To determine the area of a rectangle

#--------------------------------------#
#              Variables               #
#--------------------------------------#

print("Let's calculate the area of your rectangle in m²")

length = float(input("Enter the length of the rectangle :"))
width  = float(input("Enter the width of the rectangle :"))

#--------------------------------------#
#             Arithmetics              #
#--------------------------------------#

area = length * width

print(f"Your rectangle has an area of {area} m² !")