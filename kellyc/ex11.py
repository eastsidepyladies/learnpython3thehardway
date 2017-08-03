print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

# print("So, you\'re {age} old, {height} tall and {weight} heavy.")

# Couldn't get above commented line to print right so did it using str.format instead
# Ref: https://docs.python.org/3/tutorial/inputoutput.html
print('So, you\'re {} old, {} tall and {} heavy.'.format(age,height,weight))

# comebackto

print("What's a synonym for 'visible' or 'invisible'?", end=' ')
three = input()
print("What did you have for lunch yesterday?", end=' ')
one = input()
print("If you have an aunt or uncle, provide an adjective that describes the first one that comes to mind. If you don't have any, provide an adjective for the state of your sock drawer.", end=' ')
four = input()
print("Pick one of these construction terms: 'beam' or 'support'", end=' ')
two = input()
print("What's an animal that has a name beginning with the third letter of your first name? ", end=' ')
five = input()

print('Those were the {} days. When we thought we could {} ourselves by being very {}. This could never happen, we were just too {}. Learn from us: when life presents a chance to ride a {}, you should do it by any means neccessary.'.format(one, two, four, three, five))