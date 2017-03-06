class Car(object):

	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		
		print 'Car created: '
		self.display_all()

	def display_all(self):
		print "price:", self.price
		print "speed:", self.speed
		print "fuel:", self.fuel
		print "mileage:", self.mileage
		print "tax:", self.tax


ford_pinto = Car(50,'25mph','almost empty','20mpg')
ford_mustang = Car(30000,'150mph','full','15mpg')
lamborghini_diablo = Car(250000,'10mpg','never empty','10mpg')
toyota_prius = Car(35000,'90mph','almost full','50mpg')
honda_accord = Car(25000,'110mph','half empty','25mpg')
dodge_challenger = (30000,'120mph','empty','20mpg')
