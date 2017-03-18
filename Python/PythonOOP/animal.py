class Animal(object):
	def __init__(self,name,health=100):
		self.name = name
		self.health = health
		print 'New animal created:',self.name

	def walk(self):
		print 'Walking...'
		self.health -= 1

	def run(self):
		print "Running..."
		self.health -= 5

	def displayHealth(self):
		print "My info:"
		print "Name:", self.name
		print "Current health:", self.health

# animal = Animal('Animal')
# animal.walk()
# animal.walk()
# animal.walk()
# animal.run()
# animal.run()
# animal.displayHealth()
