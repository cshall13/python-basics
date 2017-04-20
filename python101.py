# print "Hello, World!"
# print two different things on the same line
# print ("Hello, World", "Again")

# This wont work
# print "This 
# will not let you print on 
# multiple lines"

# This will 

# print """This 
# will ignore the new lines
# unitl it sees another
# three double quotes"""


# Variable - string, number, letters, any other stuff that you can make with a keyboard 
# and  you want to stash something that's not fast, into something that is fast

# In JS..... var name = "Shane";
# In Python..... name = "Shane"
# Python is not heavily typed ( for instance C#)
# name = "Shane " + "Hall";
# first_name = "Shane";
# last_name = "Hall";
# full_name = first_name + " " + last_name
# # print full_name

# Arithmatic
# the_meaning_of_life = 40 + 2
# print the_meaning_of_life
# print the_meaning_of_life / 2
# print the_meaning_of_life % 5
# print the_meaning_of_print 
# print int(30.5 / 5.2)

# print 4 + "Joe"
# print 4 * "jOe"

# data types	(variable types)
# -Strings - English type stuff for people (in yellow)
# -Numbers - something with digits and stuff that goes with digits (-_)
# ---floats, Integer
# -Booleans - true or false. 1 0r 0.yes or no. On or off
# - lists - list of variables in one variable 
# - dictionary - variables of variables 
# - objects - deal with it later

# Strings -

# first_name = "Shane"
# last_name = "Hall"
# nickname = 'Shane "the man" Hall'
# print "Hello, {} {}".format(first_name, last_name)		**line 55 and 56 are the exact same. 55 is easier to read
# print "Hello" + first_name + " " +last_name
# Placeholders
# print "Hello, %s %s" % (first_name, last_name)
# print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)


# floats
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# make_me_a_string = str(pi_the_magic_float)
# print make_me_an_integer

# Booleans - true or false
# the_truth = True
# True or False must begin with CAPS
# print type(the_truth)
# the_lie = False
# print type(the_lie)

# Raw Input
# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")

# Conditionals
# 1 = means you want to assign the thing on the left to the thing on the right 
# 2 = means you want to compare whats on the left with whats on the right 

# if(first_name == last_name):
# 	print "Your first name is the same as your last name?"

# age = raw_input("How old are you?")
# age_as_int = int(age)
# # print type(age)
# if(age_as_int >= 21):
# 	print "You can buy beer."
# elif(age_as_int >= 18):
	# print "A few more years."
# else:
# 	print "You are underage."

# import random
# random_number =random.randint(1,10)
# # print random_number


# # Loop - keep doing something until I tell you to stop 
# not_guessed = True
# while not_guessed:
# 	guess_a_number = raw_input("Guess a number between 1 and 10.")
# 	if (int(guess_a_number) == random_number):
# 		print "You guessed the number!";
# 		not_guessed = False

# secret_number = 5
# not_guessed = True
# while not_guessed:
# 	guess_a_number = raw_input("""I'm thinking of a number between 1 and 10.
# What's the number?""")
# 	if (int(guess_a_number) == secret_number):
# 		print "Yes! You win!";
# 		not_guessed = False
# 	else:
# 		print "Nope. Guess again."

# secret_number = 5
# not_guessed = True
# while not_guessed:
# 	guess_a_number = raw_input("""I'm thinking of a number between 1 and 10.
# What's the number?""")
# 	if (int(guess_a_number) == secret_number):
# 		print "Yes! You win!"
# 		not_guessed = False
# 	elif (int(guess_a_number) < secret_number):
# 		print guess_a_number + " is too low! Guess again.";
# 	elif (int(guess_a_number) > secret_number):
# 		print guess_a_number + " is too high! Guess again.";

# import random
# secret_number =random.randint(1,10)
# not_guessed = True
# while not_guessed:
# 	guess_a_number = raw_input("""I'm thinking of a number between 1 and 10.
# What's the number?""")
# 	if (int(guess_a_number) == secret_number):
# 		print "Yes! You win!"
# 		not_guessed = False
# 	if (int(guess_a_number) < secret_number):
# 		print guess_a_number + " is too low! Guess again.";
# 	if (int(guess_a_number) > secret_number):
# 		print guess_a_number + " is too high! Guess again.";



# number_of_guesses = 5
# secret_number = 5
# keep_asking = True
# while (keep_asking):
# 	if(number_of_guesses == 0):
# 		play_again = raw_input("You ran out of guesses. Would you like to play again. Y or N?")
# 		if(play_again == "Y"):
# 			number_of_guesses = 5
# 		elif(play_again == "N"):
# 			keep_asking = False
# 			print "Goodbye, coward."		
# 	else:
# 		print ("You have %d guesses left") % (number_of_guesses)
# 	guess_a_number = raw_input("""I'm thinking of a number between 1 and 10.
# What's the number?""")
# 	if (int(guess_a_number) == secret_number):
# 		print "Yes! You win!"
# 		# keep_asking = False;
# 		number_of_guesses = 1;
# 	elif (int(guess_a_number) < secret_number):
# 		print " %d is too low! Guess again." % (int(guess_a_number))
# 		# number_of_guesses = number_of_guesses - 1		#number_of_guesses -= 1 is the same as number_of_guesses = number_of_guesses - 1
# 	elif (int(guess_a_number) > secret_number):
# 		print " %d is too high! Guess again." %(int(guess_a_number))
# 	number_of_guesses -= 1


# LISTS

# student1 = "Marissa"
# student2 = "Merilee"
# student3 = "Daniel"
# student4 = "Chris"

# print (student1,student2,student3,student4)

# list is a single variable with a bunch of nubered parts
# the number that an element is in, is called the "Index"

students = [
	"Marissa",
	"Merilee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stepen",
	"Drew"
]
# print students 
# print (students[0])
# print (students[1])
# print (students[7])
# print (students [-3])

# atlantaTeams =[
# 	"Falcons",
# 	"Braves",
# 	"Hawks",
# 	"Thrashers"
# ]

# print (atlantaTeams)

# # # to add an element to the END of a list you use the append method 
# atlantaTeams.append("Atl United")

# print (atlantaTeams)

# # # to delete an index you can use the remove method
# atlantaTeams.remove("Thrashers")
# print (atlantaTeams)

# # # we can insert into any indecie with the insert method
# atlantaTeams.insert(0,"Tom Brady's Team")

# print (atlantaTeams)

# teams_as_a_string = "Falcons, Braves, Hawks, Atl United"
# teams_as_a_list = teams_as_a_string.split(",")
# print (teams_as_a_list)

# # # sort will CHANGE the list
# atlantaTeams.sort();
# print (atlantaTeams)

# # # sorted will sort, but NOT CHANGE the list 
# copy_of_atlanta_teams = sorted(atlantaTeams)
# print (atlantaTeams)

# copy_of_atlanta_teams.reverse()
# print (copy_of_atlanta_teams)

# length_of_atlanta_teams = len(copy_of_atlanta_teams)
# print (length_of_atlanta_teams)
# print (copy_of_atlanta_teams[-1])
# print (copy_of_atlanta_teams[length_of_atlanta_teams-1])

# print len(copy_of_atlanta_teams[0])

# The other type of loop... For 
# for i in range(1,10):
# 	print i

# For Loop Format:
# [for] [what_you_want_to_call_the_thing_you_are_on] [in] [variable_looping_through]
# for student in students:
# 	# print students
# 	if (student =="Chris"):
# 		print "Welcome, Chris!"
# 	else:
# 		print "You are not Chris"

# set up a for loop.... but the range, will be 0 to len-1

# students_length = len(students)
# for i in range(0,students_length):
# 	print (students[i])

# for i in range(0,10,2):
	# print (i)

# if you want a portion of a list, you can use the [x:y] format
# This will create a COPY of the array, does not mutate or change the original
# it will start at the xth elemnt, and will stop at the yth 

# print (students)
# second_and_third = students[1:3]
# print second_and_third
# print (students)
# all_but_the_first = students[1:]
# print all_but_the_first

# a function is a piece of code that can be called from the main body of the program
# the upshot is that if you have complicated code or code that is repeated often,
# a function is your answer. 
# repeating yourself is BAD. 
# A function in python is not a function, it is a definition.
# To declare a function in python, you use "def"
# Functions ALWAYS have ()'s

# def say_hello():
	# print("Hello") print is not used to print a function. you just call the function

# say_hello()

def say_hello_with_name(name):
	print ("Hello, "+ name)

# say_hello_with_name() #this will fail 
# say_hello_with_name(Rob, Chad) #this will also fail
say_hello_with_name("Shane")

def say_hello_with_default(name, in_class = "Yes"):
	print ("Hello, "+ name)
	print "Is student in class? " + in_class 

say_hello_with_default("Carla")
say_hello_with_default("Max", "No")

# Functions always return something
def return_user_name(name):
	return name
print return_user_name("Shane")

def make_uppercase(string):
	return string.upper()

normalized_string = make_uppercase("Im A wIlD ANd craZY Guy")
print normalized_string

		






























