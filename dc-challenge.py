fullName = "Shane Hall"
age = 32

my_array = []
my_array.append(fullName)
my_array.append(age)
print (my_array)

def say_hello ():
	print ("Hello!")
say_hello()

split_name = fullName.split()
print (split_name)

def say_name():
	print ("Hello, " + split_name[0])
say_name()

def my_age(year_born):
	print (2017 - year_born)
my_age(1984)

def sum_odd_numbers():
	sum = 0
	for i in range(1,5001,2):
		sum += i
	return sum 
print (sum_odd_numbers())


