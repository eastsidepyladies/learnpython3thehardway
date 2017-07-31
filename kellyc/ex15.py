# argv allows you to pass command-line arguments to the script as a list
from sys import argv

# the two arguments in the list argv are the script and sample text files
script, filename = argv

# this creates a variable for sample text file, openned (not yet read)
txt = open(filename)

print(f"Here is your file {filename}.")
print(txt.read())

# this prompts user to supply sample text file again, unopenned
print("Type the filename again:")
file_again = input("So... what's the file called again?")

# takes input and gives it an opened status (not yet read)
txt_again = open(file_again)

# this reads and prints above
print(txt_again.read())
