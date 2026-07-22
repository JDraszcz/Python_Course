#----------------------------------------#
#             Temperature                #
#----------------------------------------#

degree = float(input("Enter the temperature :  "))
unit = input("What is the unit (F or C ) : ")

if unit == "F" :
    degree = degree * 5 / 9 - 32
    unit = "Celsius"
    print(f"The temperature in {unit} is {round(degree, 2)} {unit}")
elif unit == "C" :
    degree = degree * 9 / 5 + 32
    unit = "Farenheit"
    print(f"The temperature in {unit} is {round(degree, 2)} {unit}")
else :
    print(f"The unit {unit} is incorrect")

