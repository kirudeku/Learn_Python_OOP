class Fighters: # Fighters here is a class

	def __init__(self, name): # __init__ here is a method
		self.name = name #stuff after "." is attributes always, so name here is an attribute

qazi = Fighters("Qazi") #qazi here is an object created from a class Fighters
bob = Fighters("Melania")

print(qazi.name)
print(bob.name)