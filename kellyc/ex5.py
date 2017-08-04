# -*- coding: utf-8 -*-
# The above code can be used if you're using non-ASCII char and get an encoding error

my_name = 'Kelly C.'
my_age = 104
my_height = 97.2
my_weight = 3.4
my_eyes = 'mudbrown'
my_teeth = 'pearly'
my_hair = 'green'

# %s and %d are formatters which take a value to the right and insert it - they will be explained more later
print("Let's talk about %s." % my_name)
print("She's %d inches tall." % my_height)
print("She's %d pounds heavy." % my_weight)
print("Actually, that's not too heavy.")
print("She's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line prints three numeric values and then prints their sum
print("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))

# test out round function
print("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, round(my_age + my_height + my_weight)))
print(round(7.94568))
# this doesn't do anyting extra
print(round(round(7.94568)))
# nor does this
print(round((round(round(7.94568)))))
