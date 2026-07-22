#----------------------------------------------------#
#                   Unit Converter                   #
#----------------------------------------------------#

# Simple Exercice to calculate the weight in pounds or kilograms

#----------------------------------------------------#
#                   Variables                        #
#----------------------------------------------------#

weight = float(input("Enter your weight  : "))
unit = input("Enter the unit (Lb or Kg) : ")

#----------------------------------------------------#
#                 If Statements                      #
#----------------------------------------------------#

if unit == "Lb" :
    weight /=  2.205
    unit = "Kg"
elif unit == "Kg" :
    weight *= 2.205
    unit = "Lb"
else :
    print(f"You Should have mistaken writing this unit {unit}")

print(f"After the conversion your weight is {round(weight, 2)} {unit}")
