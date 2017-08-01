from sys import argv

script, filename = argv

# print instructions on how to abort or continue the script
print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# sets ? as prompt candy
input("?")

print("Opening the file...")
# 'w' opens the file in write mode, truncating file if it already exists (not truncate as in shorten, but truncate as in empty/deallocate)
target = open(filename, 'w')
print("Truncating the file. Goodbye!")

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Drill. Print above using one line.

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()
