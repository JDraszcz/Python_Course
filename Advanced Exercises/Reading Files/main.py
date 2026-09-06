# Let's now read the files we have created previously

# First we have to get their path 
# file_path = "Advanced Exercises/Reading Files/list.csv"

# Then we will use the with statement, and since we did use the 
# open() method previously, we will change the letter to r for "read"

# with open(file_path, "r") as file: 
    # We put the content in a variable 
    # Then we print it 
#     content = file.read()
#     print(content)


# To read a JSON file we have to use the json module as we used it to write the file
# import json

# with open(file_path, "r") as file:
#     content = json.load(file)
#     print(content)


# Last we have to read the csv file, first we import the csv module

# import csv

# with open(file_path, "r") as file:
    # First let's have access to the file
#     content = csv.reader(file)
    # However to write it we did had to write it row by row
    # The concept is the same in order to read it
#     for line in content:
#         print(line[3])


# There's an error which indicates that's I'm out of range which starts at 0 
# illogical
