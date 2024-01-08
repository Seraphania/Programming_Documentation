##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Task 1: Open and Read a File
#   1:  Learn about file handling in Python and understand the basics of reading from and writing to files
#   2:  Create a new text file (you can do this manually) with some sample text.
#   3:  Write a Python script that opens the file, reads its content, and prints it to the console.
#   4:  Modify the script to prompt the user for a new line of text, and then append that line to the existing file.

file_path = r"C:\Python\Learning\2_Functions_and_Modules\FileToBeHandled.txt"
with open(file_path, 'r') as file:
    read_data = file.read()
    print("The file contains the following:")
    print(read_data)
with open(file_path, 'a') as file:
    file.write(input("What would you like to add? "))
    