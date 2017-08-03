x = "There are %d types of people in the world." % 10
binary = "binary"
# convert do underscore not to the contraction don't
do_not = "don't"
# first time I ran this I forgot the last %
y = "Those who know %s and those who %s" % (binary,do_not)

print(x)
print(y)

print("Hm, what did I say? %r." % x)
print("What else did I say? '%s'." % y)

# sets variable as equal to boolean value
hilarious = False
# creates variable with yet to be defined formatter
joke_evaluation = "Funny, huh?! %r"

# this passes a value to the formatter and prints what's assigned above
print(joke_evaluation % hilarious)

# this prints as expected
# j = "This is merely a test. %r"
# this prints as expected
j = "This is merely a test. %s"
# this prints a 0 instead of False
# j = "This is merely a test. %d"

# %r and %s behave as expected but not %d
print(j % hilarious)

w = "Yoohoo, over here on the left..."
e = "Hidey-ho, over here on the right."

print(w + e)
