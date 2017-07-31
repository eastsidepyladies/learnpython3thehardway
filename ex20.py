from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")
    
current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("\n\nNow let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

for i in range(3):
    print_a_line(i + 1, current_file)
    