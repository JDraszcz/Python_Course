#----------------------------------------------------------------#
#                           Concession                           #
#----------------------------------------------------------------#

# We will try to create a menu with an associate price

menu = {"popcorn" : 1.00, 
        "hot dog" : 2.00, 
        "giant pretzel" : 2.00, 
        "asst candy" : 1.00, 
        "soda" : 1.00, 
        "bottled water" : 1.00}

cart = []

total = 0

for key, value in menu.items() :
    print(f"{key:10}  : {value:.2f}")

while True :
    food = input("Select by the number of item what you desire (Q to quit) : ").lower()
    if food == "q" :
        break
    elif menu.get(food) is not None:                    
        cart.append(food)
        print(f"The item {food} has been added to your cart")
    else :
        print("We don't have this on our menu")

for items in cart : 
    total += menu.get(items)

multiples = list(dict.fromkeys(cart))

print("------------------Your Cart------------------")
for element in multiples: 
    print(f"{element} : x{cart.count(element)}")

print("---------------------------------------------")

print(f"The total would be ${total}")