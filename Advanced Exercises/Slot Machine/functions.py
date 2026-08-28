import random
import time

balance = 100

bet = 0


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for i in range (3)]

# This formulation create the list registered as spin_row()



def print_row(row):
    global results
    print("\n Gambling Starting")
    time.sleep(2)
    print(" | ".join(row))


def payout(row): 
    global balance
    global bet
    if row[0] == row[1] == row[2] :
        print("Big Win, multiplier x2 !!")
        bet *= 2
        balance += bet
        print(f"Your Balance is now ${balance}")
    elif (row[0] == row[1]) or (row[1] == row[2]) or (row[0] == row[2]) :
        print("Little Win, multiplier x1.25 !")
        bet *= 1.25
        balance += bet
        print(f"Your Balance is now ${balance}")
    else:
        print("You Just lost, let's try again")


def bet():
    global bet
    global balance
    user_bet = input("Please enter your bet : ")
    try:
        bet = float(user_bet)
    except ValueError: 
        print("Please enter a valid value")

    if bet > 0:
        balance -= bet
        print(f"Your balance is actually ${balance}")
        return bet
    else :
        print("Your bet must be greater than 0")
        return 


def home():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   ")
    print("                                                           ")
    print("                                                           ")
    print("              Welcome to our slot machine !                ")
    print("                                                           ")
    print(f"Your Balance is ${balance:.2f}                             ")
    print("                                                           ")
    print("Please choose an option :                                  ")
    print("                                                           ")
    print("1. Start game                                              ")
    print("                                                           ")
    print("2. Exit                                                    ")
    print("                                                           ")
    print("                                                           ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   ")

def option():
    user_input = input("Enter Your Option (1/2) : ")
    try :
        user_input = int(user_input)
        return user_input
    except ValueError :
        print("Please enter a valid value.")
        return


if __name__ == "__main__" :
    print("You are not supposed to execute the code from there")