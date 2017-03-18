from animal import Animal

class Dog(Animal):
	def __init__(self):
		super(Dog,self).__init__(self)
		self.health = 150

	def pet(self):
		print "Petting..."
		self.health += 5

fido = Dog('Fido')
fido.walk()
fido.walk()
fido.walk()
fido.run()
fido.run()
fido.pet()
fido.displayHealth()