# mystuff = { 'apple': "I AM APPLES!"}
# print (mystuff['apple']) # get apple from dict

# import mystuff
# mystuff.apple() # get apple from module

# print(mystuff.tangerine) #get tangerine from module, only now its a variable

# instead of import, you instantiate(create) a class in python

class Mystuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	
	def apple (self):
		print("I AM CLASSY APPLES!")
		

		
# Instanciate an object
thing = Mystuff()
thing.apple()
print(thing.tangerine)