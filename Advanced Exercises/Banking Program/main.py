import functions 

is_running = True

def main():

    global is_running

    while is_running:
        functions.home()
        match functions.choice():
            case 1:
                functions.show_balance()
            case 2:
                functions.deposit()
            case 3:
                functions.withdraw()
            case 4:
                break
            case _ :
                print("Please choose a valid option")

        

if __name__ == "__main__" :
    main()
    print("Have a good day")
