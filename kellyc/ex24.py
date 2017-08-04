print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is now.
"""

print("-----------------")
print(poem)
print("-----------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# the secret formula comes up with # of beans, jars and crates
# start_point is provided as started in this function. If started is replaced with start_point in the two places it appears in the code, it runs the same
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# three values returned above assigned to three variables below
# if you change start_point to started in the below, it won't run as started has not been defined
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
