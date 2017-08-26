# Doing things with lists

# This assigns a string to variable ten_things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not ten things in this list. Let's fix that.")

# this splits the string assigned to ten_things by empty spaces, creating a list
stuff = ten_things.split(' ')

# Translating these functions like so below did not work (NameError: name 'split' is not defined)
# stuff = split(ten_things, ' ')

# this assigns another list to the variable more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# checks if the stuff list contains ten items and runs following lines until condition is met
while len(stuff) != 10:
    # this creates a variable to contain one item "popped off" of the more_stuff list
    next_one = more_stuff.pop()
    # next_one = pop(more_stuff)
    # this handy-dandy print statement lets you know which item was popped off
    print("Adding: ", next_one)
    # this appends the popped off item to stuff
    stuff.append(next_one)
    # append(stuff, next_one)
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
# print(pop(stuff))
# This joins the items in the list with spaces betwixt
print(' '.join(stuff))
# print(join(' ', stuff))
# This joins the 4th and 6th items in the list with an octothorpe betwixt
print('#'.join(stuff[3:5]))
# print(join('#', stuff[3:5]))



colors = "brown yellow red taupe fuschia"
more_colors = ["magenta", "lilac", "primrose", "burnt-orange", "salmon", "green"]

my_colors = colors.split(' ')
print("Here's a list of the colors we are starting with: ", my_colors)

while len(my_colors) != 9:
    new_color = more_colors.pop()
    print("Let's add", new_color, "to the list.")
    my_colors.append(new_color)
    print(f"There are now {len(my_colors)} colors in the list.")

while len(my_colors) != 10:
    new_color = more_colors.pop()
    print("Almost there. Let's add ", new_color, "to the list.")
    my_colors.append(new_color)
    print(f"There are finally {len(my_colors)} colors in the list.")

print(my_colors)
print(my_colors.pop())
sorted_colors = sorted(my_colors)
print(sorted_colors)
sorted_in_reverse_colors = sorted(my_colors, reverse=True)
print(sorted_in_reverse_colors)
