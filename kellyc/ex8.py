formatter = "{} {} {} {}"

# match input of four arguments to formatter string defined on line 1
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# the results of passing formatter as the arguments
print(formatter.format(formatter, formatter, formatter, formatter))
# four strigns passed as arguments - new lines don't make a difference
print(formatter.format(
    "Warm days",
    "without air conditioning",
    "make good days",
    "for popsicles"
))