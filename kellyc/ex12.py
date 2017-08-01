# another way to do inputs...
# this assigns what someone inputs for name to y
y = input("Name? ")
age = input('How old are you? ')
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print("So you're {age} old, {height} tall, {weight} heavy.")
print(age)

# Notes
# from pydoc and elsewhere
# open is the preferred way to open a files
# os exports a lot of functions... programs that use 'os' stand a better chance of being portable between devices... but - they must leave pathname manipulation to os.path (split/join)
