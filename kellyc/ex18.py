# creates function def (for define) and gives it a name
def print_two(*args):
# this unpacks provided arguments
	arg1, arg2 = args
# this prints them
	print(f"arg1: {arg1}, arg2: {arg2}")

# unpacking is uneccessary, you can just print them like so
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
	print("I got nothin'.")


print_two("Peter","Piper")
print_two_again("Peter","Piper")
print_one("First!")
print_none()
