## Animal is-a object (yes, sort of confusing) look at the extra credit 
class Animal ( object ): 
	pass 

## Is an Animal object
class Dog ( Animal ): 

	def __init__ ( self , name ): 
		## dog animal has a name
		self . name = name 
 
## Is an Animal object
class Cat ( Animal ):

	def __init__ ( self , name ): 
		## cat animal has a name
		self . name = name 

## Is an object
class Person ( object ): magic? 

	def __init__ ( self , name ): 
		## person has a name
		self . name = name 
 
		## Person has-a pet of some kind 
		self . pet = None 

## Is an Person object
class Employee ( Person ): 
 
	def __init__ ( self , name , salary ): 
		## employee is a person  
		super ( Employee, self ) . __init__ ( name )
		## employee has a salary
		self . salary = salary 
 
## is an object 
class Fish ( object ): 
	pass 
 
## Is a Fish object
class Salmon ( Fish ): 
	pass 
 
## Is a Fish object
class Halibut ( Fish ): 
	pass 

		
## rover is-a Dog animal
rover = Dog ( "Rover" ) 

## satan is a cat animal
satan = Cat ( "Satan" ) 

## mary is a person 
mary = Person ( "Mary" ) 

## mary has a pet cat
mary . pet = satan 

## frank is a employee person
frank = Employee ( "Frank" , 120000 ) 

## frank has a pet dog
frank . pet = rover 

## flipper is a fish
flipper = Fish () 

## crouse is a Salmon fish
crouse = Salmon () 

## harry is a halibut fish
harry = Halibut ()