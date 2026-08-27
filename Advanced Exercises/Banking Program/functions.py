
balance = 100 

def show_balance():
    print(f"Your Current Balance is : ${balance}")


def deposit():
    global balance  # To access the global variable
    ammount = input("How much would you like to deposit : ")
    try:
        ammount = float(ammount)
    except ValueError:
        print("The value you have entered can not be add.")
        return

    if ammount > 0:
        balance += ammount
        print(f"Your balance is now ${balance}")

        return balance
    else:
        print("The ammount you have entered is less than 0")
        return


def withdraw():
    global balance
    ammount = input("How much would you like to withdrawn : ")
    try:
        ammount = float(ammount)
    except ValueError : 
        print("The value you have entered can not be add")
        return

    if balance < ammount:
        print("You don´t have any money")
        return
    else:
        balance -= ammount
        print(f"Your balance is now ${balance}")
        return balance



def home():
    print("&&&&&&&&&&&&&&&")
    print("Banking Program")
    print("               ")
    print("1. Show Balance")
    print("2. Deposit     ")
    print("3. Withdrawal  ")
    print("4. Exit        ")
    print("               ")
    print("&&&&&&&&&&&&&&&")

def choice():
    user_choice = input("Choose an option (1-4) : ")
    try:
        user_choice = int(user_choice)
        return user_choice
    except ValueError:
        print("Please enter a valid Value")
        return 


if __name__  == "__main__" :
    print("You are not supposed to execute the code from there")