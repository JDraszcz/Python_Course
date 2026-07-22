#---------------------------------------------------------------#
#                         Shopping Cart                         #
#---------------------------------------------------------------#

# We'll let the user choose his item, the price and how much he wants
# Then we are going to calculate the price

#---------------------------------------------------------------#
#                           Variables                           #
#---------------------------------------------------------------#


item = input("What item do you desire ? :")
price = float(input("How much does it cost ? :"))
quantity = float(input("How many would you like to purchase ? :"))

#---------------------------------------------------------------#
#                       Arithmetics                             #
#---------------------------------------------------------------#

new_price = price * quantity

print(f"For the item {item}, at {price} each and for {quantity} of those you will have to pay ${price}")