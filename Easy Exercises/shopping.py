#-----------------------------------------------------------------------------#
#                               Shopping                                      #
#-----------------------------------------------------------------------------#

# In this exercise we are going to ask the user the food he wants and set the price
# Then we are going to print this and finally give them the total


#-----------------------------------------------------------------------------#
#                              Variables                                      #
#-----------------------------------------------------------------------------#

foods = []
prices = []
total = 0

#-----------------------------------------------------------------------------#
#                                   Loops                                     #
#-----------------------------------------------------------------------------#

while True :
    food = input("Enter the food you would like to buy (e for exit) : ")
    if food == "e" or food == "E":
        break
    else :
        foods.append(food)
        price = float(input(f"Please set the price for {food} : "))
        if price <= 0.0:
            print("We are not giving food for free. End of your shopping session.")
        else: 
            prices.append(price)
            print(f"Your article {food} for ${price} has been added to your cart")

#-----------------------------------------------------------------------------#
#                               Resume                                        #
#-----------------------------------------------------------------------------#

print("Here's all the food you ordered :")
for food in range(len(foods)):
    print(foods[food], end=", ")

for price in range(len(prices)) :
    total += prices[price]
    
print(f"Your total is ${total}")