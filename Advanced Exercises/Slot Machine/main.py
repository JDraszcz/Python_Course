from functions import *


def main():
    is_running = True
    while is_running:
        home()
        match option():
            case 1:
                bet()
                row =  spin_row()
                print_row(row)
                print("\n")
                payout(row)
            case 2: 
                break
            case _:
                print("Please choose a valid value (1 or 2)")

    print("Have a good day !")

if __name__ == "__main__" :
    main()