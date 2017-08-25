the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this takes each item in the list and prints the statement below
# the individual items in the list are all assigned to the variable "number"
for number in the_count:
    print(f"This is the count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}.")

# this creates an empty list
elements = []

# this uses the range function to do a 0-5 count
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # this appends the items created by the range function into the elements list
    elements.append(i)
    # elements.reverse() # this reorders the list? 5,3,1,2,4
    # elements.copy() # this doesn't seem to do anything

# this prints a statement with each item of elements inserted
for i in elements:
    print(f"Element was: {i}")

# Notes
# lists => containers of *ordered* things within square brackets
# Ranges are immuatable sequence types which are commonly used for looping a specific number of times in for loopsself.
# An advantage of range over list is that they use a small amount of memory no matter the size of the represented range, due to only including values for start, stop, and step
# https://docs.python.org/3/library/stdtypes.html#typesseq-range
