#-----------------------------------------------------#
#                    Shipping label                   #
#-----------------------------------------------------#

# I didn't really understand this exercise but we are 
# going to use *args and *kwargs to create a shipping label

def shipping_label(*id, **adress):
    for arg in id :
        print(arg, end=" ")
    print()
    for cat, value in adress.items(): 
        print(f"{cat} : {value}")


# The following if statement is used in order
#  to prevent None printing
# If you need to print a zip code that is not defined it will print None
# To prevent that we are going to use that if statement

    if "zip" in adress:
        print(f"Your zip code is {adress.get("zip")}")

shipping_label("Mr.", "John", "Doe",
               country="",
               zip="12",
               city="",
               street=""
               )