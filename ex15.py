from sys import argv

#Read in name of this script and filename of where file is located
script, filename = argv

#This will move the file's contents into memory
txt = open(filename)

#prints out the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

#Lets you open any file you want and reads it back
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
