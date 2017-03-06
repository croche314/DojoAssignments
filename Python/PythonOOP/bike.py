class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
		print "new bike created!"

	def displayInfo(self):
		print "price:", self.price
		print "maximum speed", self.max_speed
		print "total miles: ", self.miles

	def ride(self):
		print "Riding..."
		self.miles += 10

	def reverse(self):
		print "Reversing..."
		self.miles -= 5

whoopty = Bike(5,'10mph')
bmx = Bike(200,'30mph')
mountain = Bike(1000,"50mph",1000)

print "bmx -->", bmx.displayInfo()
bmx.ride()
bmx.reverse()
print bmx.miles