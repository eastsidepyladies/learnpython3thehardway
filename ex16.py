from sys import argv

script, filename = argv

print("Today we are creating haiku's")
print(f"We will save it in the file {filename} you provided")

txt = open(filename)
print("Currently your file contains the following: ")
print(txt.read())
txt.close()

print(f"We're going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you are ok with this, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Erasing the content in file. Goodbye!")
target.truncate()

print("Now I'm going to ask you to write a haiku")

line1 = input("1st line (5 syllables): ")
line2 = input("2nd line (7 syllables): ")
line3 = input("3rd line (5 syllables): ")
print("Awesome. Let me assemble your haiku")


target.write(line1)
target.write("\n") #line break
target.write(line2)
target.write("\n") #line break
target.write(line3)
target.close()

print("Would you like me to read your new file back?")
print("hit CTRL-C (^C). to close this program")
print("otherwise, hit RETURN.")
input("?")

print("Here is your new file")

txt = open(filename)
print(txt.read())
txt.close()