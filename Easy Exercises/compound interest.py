#------------------------------------------------------#
#                   Interest rate                      #
#------------------------------------------------------#


# We're going to ask an ammount of money, a rate and a period
# To give the user the money it will become

#------------------------------------------------------#
#                    Variables                         #
#------------------------------------------------------#

initial_ammount = 0
initial_rate = 0
inital_period = 0

#------------------------------------------------------#
#                   While Statements                   #
#------------------------------------------------------#

while initial_ammount <= 0:
    initial_ammount = float(input("Please enter a valid ammount : "))
    print(f"The selected initial ammount is ${initial_ammount}")
    if initial_ammount <= 0 :
        print(f"The Value ${initial_ammount} is not a correct ammount.")


while initial_rate <= 0:
    initial_rate = float(input("May now insert a correct rate : "))
    print(f"The current rate has switched to {initial_rate}.")
    if initial_rate <= 0:
        print(f"The rate {initial_rate} is uncorrect.")

while inital_period <= 0:
    inital_period = float(input("Please enter the selected period in years : "))
    print(f"The calculation will proceed for the period of {inital_period} years")
    if inital_period <= 0:
        print("Please enter a correct time period.")

#------------------------------------------------------#
#                   Calculation                        #
#------------------------------------------------------#

# new_ammount = initial_ammount*(1 + initial_rate/100)**inital_period

new_ammount = initial_ammount* pow((1+ initial_rate/100), inital_period)

# print(f"In {inital_period} years, your initial ammount of ${initial_ammount} with an interest of {initial_rate} will become ${round(new_ammount,2)} !")
print(f"In {inital_period} years, your initial ammount of ${initial_ammount} with an interest of {initial_rate} will become ${new_ammount:.2f} !")