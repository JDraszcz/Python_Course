# Inspired from the exercise from the video

#--------------------------------------------#
#           Username Verification            #
#--------------------------------------------#


username = input("Write your Username : ")
length = len(username)
spaces = username.find(" ")
# remove = username.replace(" ", "")
no_digits = username.isalpha()

if length <= 12 :
    if spaces <= 0 : 
        if not no_digits : 
            print("Your username must not contain digits")
        else :
            print(f"Your username {username} has been registrated !")

    else : 
        print(f"Your username can't have spaces")

else :
    print(f"Your username is too long, 12 characters maximum and you are at {length}")


# This is a fully functionnal system but the best way is by using elif
# If all the restrictions are respected we can print the username