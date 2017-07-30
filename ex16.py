import sys 
import time

script, filename = sys.argv

print("Today we are creating haiku's")
print(f"We will save it in the file {filename} you provided")

next = input(f'Do you want to see what is inside {filename}? Y or N: ')

if next == 'Y':
    
    txt = open(filename)
    print("Currently your file contains the following: ")
    line = txt.readline()
    
    while (next != "N" and next != "n"):
        print(line)
        line = txt.readline()
        sys.stdout.flush()
        time.sleep(5)
        print(line)
        line = txt.readline()
        sys.stdout.flush()
        time.sleep(1)
        next = input('More? Y or N: ')
    txt.close()
    
print(f"We're going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you are ok with this, hit RETURN.")

input("?")

print("Opening the file...")
sys.stdout.flush()
target = open(filename, 'w')
time.sleep(5)

print("Erasing the content in file. Goodbye!")
target.truncate()
sys.stdout.flush()
time.sleep(5)


print("Now I'm going to ask you to write a haiku")
sys.stdout.flush()
time.sleep(1)

line1 = input("1st line (5 syllables): ")
line2 = input("2nd line (7 syllables): ")
line3 = input("3rd line (5 syllables): ")
print("Awesome. Let me assemble your haiku")


target.write(line1)
target.write("\n") #line break
target.write(line2)
target.write("\n") #line break
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()

print("Would you like me to read your new file back?  Y or N: ")
response = input(">")

if response == "y" or response == "Y":
    print("Here is your new file")
    
    txt = open(filename)
    print(txt.read())
    txt.close()