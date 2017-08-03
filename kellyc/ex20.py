from sys import argv

script, input_file = argv

# this function reads and then prints input file as a formatted string literal
def print_all(f):
    print(f.read())

# IMPORTANT: seek deals with bytes, not lines. f.seek(0) goes to the beginning of file not by seeking to the first(0) line, but because 0 bytes marks the very beginning of the file, before anything constituting bytes are introduced
def rewind(f):
    f.seek(0)

# creates a print function that takes and formats a line based on given line number
def print_a_line(line_count, f):
    # prints line number and formatted string literal
    print(line_count, f.readline())

# creates variable with the openned input file as value
current_file = open(input_file)

# this print statement includes a new line regex
print("First let's print the whole file:\n")

# uses print_all function to print what's assigned to current_file (that would be input_file)
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# uses rewind function to assume position of the first line in current_file
rewind(current_file)

print("Let's print three lines:")

# this variable establishes current_line as 1
current_line = 1
# use of this function prints the line number, 1, and the corresponding text, first line of text in the current_file
print_a_line(current_line, current_file)

# this creates a iterator to move from one line directly to the next
current_line = current_line + 1
# use of this function prints the line number and line contents of whatever line the iterator is on
print_a_line(current_line, current_file)

# same as above
current_line = current_line + 1
print_a_line(current_line, current_file)


# Notes
# The f here is a variable that is a file that has a "read head" set, meaning that it can be handled as an openned file, with internal positions

#  =+ is a contraction for operations. x = x+ y means the same thing as x =+ y
