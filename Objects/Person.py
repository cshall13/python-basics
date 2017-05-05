class Person(object):
	def __init__(self,name,gender,cell):
		self.name = name
		self.gender = gender
		self.species = "Human"
		# self.phone {
		# 	cell: "cell"
		# 	home: "Who has a home phone anymore?"
		# }
	
	def greet(self, other_person):
		print "Hello %s, I am %s!" % (other_person, self.name)

	def print_contact_info(self):
		if(self.phone['cell'] != ""):
			print "%s's number is %s" % (self.name, self.phone['cell'])

shane = Person("Shane", "male", 404-717-5661)
print shane.name + " " + shane.gender
print shane.name, shane.gender, 
print shane.species

merilee = Person("Merilee", "female",123-456-7890)
print merilee.species
merilee.species = "Robot"
print merilee.species
shane.greet ("Rob")

class Vehicle(object):
	def __init__(self, make2, model2, year2):
		self.make = make2
		self.model = model2
		self.year = year2

	def print_info(self):
		print self.year, self.model, self.make

	def change_year(self, new_year):
			self.year = new_year

david_cummings_car = Vehicle("Mcclaren", 'Mp4-12c', 2013)
david_cummings_car.print_info()
david_cummings_car.change_year(2015)
david_cummings_car.year = 2015

