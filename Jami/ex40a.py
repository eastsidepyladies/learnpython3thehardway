# dict style
#
# mystuff = { 'apple': "I AM APPLES!"}
# print (mystuff['apple']) # get apple from dict


# module style
#
# import mystuff
# mystuff.apple() # get apple from module
#
# print(mystuff.tangerine) #get tangerine from module, only now its a variable


# class style
# instead of import, you instantiate(create) a class in python

class Mystuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	
	def apple (self):
		print("I AM CLASSY APPLES!")
		

# class style	
#	
# Instanciate an object
thing = Mystuff()
thing.apple()
print(thing.tangerine)