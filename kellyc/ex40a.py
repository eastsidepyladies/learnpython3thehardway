import ex40_mystuff

mystuff = {'apple' : "I am merely apple."}
print(mystuff['apple'])

# prints from mystuff
ex40_mystuff.apple()

# prints from mystuff
print(ex40_mystuff.tangerine)

# Doesn't work?
# ex40_mystuff['apple']


print(ex40_mystuff.testing['test1'])
print(ex40_mystuff.testing)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apples(self):
        print("I am classy apples?")

thing = MyStuff()
thing.apples()
print(thing.tangerine)
