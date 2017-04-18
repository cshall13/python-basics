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
# name = "Shane" + "Hall";
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
# -Strings - English type stuff for peopl (in yellow)
# -Numbers - something with igits and stuff that goes with digits (-_)
# ---floats, Integer
# -Booleans - true or false. 1 0r 0.yes or not. On or 

# Strings -

# first_name = "Shane"
# last_name = "Hall"
# print "Hello, {} {}".format(first_name, last_name)
# print "Hello" + first_name + " " +last_name
# Placeholders
# print "Hello, %s %s" % (first_name, last_name)
# print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)


# floats
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer

# Booleans - true or false
# the_truth = True
# True or False must be in CAPS
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

secret_number = 5
not_guessed = True
while not_guessed:
	guess_a_number = raw_input("""I'm thinking of a number between 1 and 10.
What's the number?""")
	if (int(guess_a_number) == secret_number):
		print "Yes! You win!";
		not_guessed = False
	else:
		print "Nope. Guess again."

# secret_number = 5
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

# import random
# random_number =random.randint(1,10)
# not_guessed = True
# while not_guessed:
# 	guess_a_number = raw_input("""I'm thinking of a number between 1 and 10.
# What's the number?""")
# 	if (int(guess_a_number) == random_number):
# 		print "Yes! You win!"
# 		not_guessed = False
# 	if (int(guess_a_number) < random_number):
# 		print guess_a_number + " is too low! Guess again.";
# 	if (int(guess_a_number) > random_number):
# 		print guess_a_number + " is too high! Guess again.";





























