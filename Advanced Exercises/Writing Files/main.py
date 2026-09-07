# This python file is an exercise to create output files
# I think that we are going to need to os module so let's import it
# import os

# Then let's create a variable with the output

# output = "Hi Everyone !" \
# "The File you are reading has been made using python" \
# "The text has been written in a python file" \
# "And the output is the text file you are reading" \
# "Isn't it excellent !!" \

# Then let's create a variable for the path
# PS : The code is executed from Python_Course

# output_path = "Advanced Exercises/Writing Files/text.txt"

# My mistake we are not using the os module but the with statement
# Let's explain everything then let's code it 
# with : Allows us to open a file and close it when the task is finished
# open(output_path, "w"): function returning the file object
# output_path : Go search for the file and create it if needed
# "w" : means write (like in cmd)
# "x" is for writing only if the file doesn't exist
# "a" means append, it can add code in the file already created
# "r" means read

# Let's now write the code 

# with open(file= output_path, mode= "w") as file:
    # Then a write() built-in method already exists
    # So let's use it
#     file.write(output)
#     print(f'File {output_path} successfuly created')


# let's now output a JSON file
# To create a JSON file, the json module is required

# import json



# people = {
#     "name" : "Jordan",
#     "last name" : "Draszcz",
#     "age" : 17,
#     "address" : "5b Liecourt",
#     "zip" : 60110,
#     "city" : "Esches"
# }

# The rest of the code is similar to the previous one
# We just add the dump() method to convert our dictionnary into
# a json file 


# output_path = "Advanced Exercises/Writing Files/table.json"

# with open(output_path, "x") as file:
    # the dump method need 2 arguments : dictionnary and file  
    # To make it more readble, you can use the indent attribute 
#     json.dump(people, file, indent = 5)
#     print(f"JSON file has been created at {output_path}")


# Let's now do the same for csv files
# Means coma separated values
# It's a raw text, compatible with excel and others
# First let's create a list
# The csv module is required

import csv

list = [["Name", "Age", "Job"],
        ["Jordan", 17, "Student"], 
        ["Jean", 43, "Cashier"], 
        ["Lune", 22, "Adventurer"]
        ]

output_path = "Advanced Exercises/Writing Files/list.csv"
# The rest works the same, only the written part is different like is JSON

with open(output_path, "w", newline="") as file:
    write = csv.writer(file)
    # The upper line creates the file but we still have to write the rows one by one
    # So let's use a for loop
    for people in list:
        write.writerow(people)
    print(f"The CSV file has been succesfully created at {output_path}")