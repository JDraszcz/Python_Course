# This Complete Exercise will be made using the Bro Code video
# And will be detailled as much as possible

# We will first need to import to os (operating system module)
# To access computer components
# import os
# This is a big module so it could be nice to read the documentation




# 2 kind of paths exists :
# Relative : folder/file.txt
# Absolute : C:/Users/Folder/file.txt
# First we are going to work with relative ones
# We will create a readme file in the same folder to do our first file detection
# file_path = "Advanced Exercises/File Detection/readme.txt"
# Since the file is in the same folder we only need the name
# let's now use the os module to find it 

# if os.path.exists(file_path):
    # This if statement will return a boolean value
    # Let's now verify if the path is a file or a folder
    # For this we are using a print statement
#     if os.path.isfile(file_path):
#         print("This path lead to a file")
#     elif os.path.isdir(file_path):
#         print("This path lead to a directory")
# else :
#     print("The file doesn't exist")
