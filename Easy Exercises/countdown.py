#---------------------------------------------------------------#
#                       Countdown                               #
#---------------------------------------------------------------#

# Using loops we are going to create a countdown program
# We will ask the user to enter a time in second
# The we will print the remaining time every second


import time

#---------------------------------------------------------------#
#                       Variables                               # 
#---------------------------------------------------------------#

desired_time = int(input("What time do you want (in seconds) : "))


#---------------------------------------------------------------#
#                           Loops                               #
#---------------------------------------------------------------#

for i in range(desired_time, 0, -1) :
    hours = int((i / 3600))
    minutes = int((i / 60) % 60)
    seconds = i % 60
    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)


print(f"Your {desired_time} seconds(s) timer has finished !")