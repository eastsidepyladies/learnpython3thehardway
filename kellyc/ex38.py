# Doing things with lists

# This assigns a string to variable ten_things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not ten things in this list. Let's fix that.")

# this splits the string assigned to ten_things by empty spaces, creating a list
stuff = ten_things.split(' ')
# this assigns another list to the variable more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# checks if the stuff list contains ten items and runs following lines until condition is met
while len(stuff) != 10:
    # this creates a variable to contain one item "popped off" of the more_stuff list
    next_one = more_stuff.pop()
    # this handy-dandy print statement lets you know which item was popped off
    print("Adding: ", next_one)
    # this appends the popped off item to stuff
    stuff.append(next_one)
    # this prints how many items are in the list thus far
    print(f"There are {len(stuff)} items now.")

# this prints stuff once it has ten items (note how lists are punctuated)
print("There we go: ", stuff)

print("Let's do some things with stuff.")

# this prints second item in list
print(stuff[1])
# this prints the first item before the end
print(stuff[-1])
# This pops the last item off the list and prints what was popped
print(stuff.pop())
# This joins the items in the list with spaces betwixt
print(' '.join(stuff))
# This joins the 4th and 6th items in the list with an octothorpe betwixt
print('#'.join(stuff[3:5]))
