# In this project we are going to create a fully fonctionnal alarm clock
# A sound might be needed
# We are going to use the time module
# I'm not going to code my idea but here it is
# We will import the date and timedate module
# We will set the targeted date using the timedate module
# We will use the sleep method of the time module in a 
# while loop
# And finally we ring the bell 

# Here's the code from the video
import time
import datetime
# The pygame library is used to play a sound

clock = datetime.datetime(2026, 9, 7, 15, 0, 0)
actual = datetime.datetime.now()

print(clock)

while actual < clock : 
    time.sleep(1)
    actual = datetime.datetime.now()
    format = actual.strftime("%H %M %S")
    print(format)

# Just add the pygame method to play a sound

print("Time's up !")
