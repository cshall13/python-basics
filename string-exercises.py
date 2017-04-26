a_string = "MUFC is religion"
print a_string.upper()
# print a_string.capitalize()

# Reverse a string
# a_list = list(a_string)
# a_list.reverse()
# print("".join(a_list))
# or
# characters_from_string = []
# for character in a_string:
# 	characters_from_string.append(character)
# characters_from_string.reverse()
# print("".join(characters_from_string))

# leetspeak_string = ("""I need to write a dang paragraph. It's actually really hard 
# to do without having anything to write about. So essentially I think you just end up writing 
# jibberish. This is hopefully the least cool thing that I will do all day.""")

# crazy_list = leetspeak_string.split(" ")
# # print crazy_list
# result = ""

# for paragraph in leetspeak_string:
# 	if paragraph.upper() == "A":
# 		result += "4"
# 	elif paragraph.upper() == "E":
# 		result += "3"
# 	elif paragraph.upper() == "G":
# 		result += "6"
# 	elif paragraph.upper() == "I":
# 		result += "1"
# 	elif paragraph.upper() == "0":
# 		result += "0"
# 	elif paragraph.upper() == "S":
# 		result += "5"
# 	elif paragraph.upper() == "T":
# 		result += "7"
# 	else:
# 		result += paragraph
# print result

# Long-long vowels 

# stupid_word = "fool"
# result = ""
# current = ""
# previous = ""

# for i in range(0,len(stupid_word)):
# 	current = stupid_word[i]
# 	if (current == previous):
# 		result = result + 4 * current
# 	else:
# 		result = result + current
# 	previous = current
# print result

# Ceasar Cipher
# Use your solution to decipher the following text: 
# "lbh zhfg hayrnea jung lbh unir yrnearq"

# def decrypt_function(encrypted_letter):
# 	try:
# 		number = encrypted_list.index(encrypted_letter)
# 	except ValueError:
# 		# Do this!
# 		decrpyted_message.append(encrypted_letter)
# 	else:
# 		decrpyted_message.append(decrpyted_list[number])

# message = "lbh zhfg hayrnea jung lbh unir yrnearq!"
# decrpyted = "abcdefghijklmnopqrstuvwxyz"
# encrypted = "nopqrstuvwxyzabcdefghijklm"
# message_list =  list(message)
# decrpyted_list = list(decrpyted)
# encrypted_list = list(encrypted)
# decrpyted_message = []

# for i in range(0,len(message_list)):
# 	decrypt_function(message_list[i])

# final_decrypted_message = "".join(decrpyted_message)
# print (final_decrypted_message)



# 1-10s
# for i in range(1,11):
# 	print i


# n to m
# start_number = int(raw_input("Pick a number to start with: "))
# end_number = int(raw_input("Choose your number to end with: "))
# for i in range(start_number, end_number +1):
# 	print i
 
# for i in range(0,10):
# 	print i

# for i in range(1,11,2):
# 	print i

# print a square


# numb_list = [1,2,3,4,5,6,7,8,9]
# ans = sum(numb_list)
# print ans

# print a triangle 

# height = 4
# for i in range(1,height+1):
# 	spaces = (height - i) * 2 * " "
# 	stars = ((i - 1) * 2 + 1) * "* " 
# 	print (spaces + stars)

# Bonus: Print a Banner

# input_text = "Good morning, Vietnam!"
# for i in input_text:
# 	print(len(input_text) * "*" + "**")
# 	print ("*" + input_text + "*")
# 	print(len(input_text) * "*" + "**")
# 	break

# Print a square

# height = 4
# for i in range(1,height+1):
# 	# print the padding (spaces)
# 	spaces = (height-i) * 2 * " "
# 	stars = ((i - 1) * 2 + 1) * "* "
# 	print ( spaces + stars ) 


# def print_star():
# 	spaces = " " * (space_count / 2)
# 	stars = "*" * star_count
# 	print ( spaces + stars + spaces ) 
# total_width = 10
# star_count = 1
# space_count = total_width - star_count
# loop_count = 1
# while loop_count <= 10:
# 	if(star_count % 2 == 1):
# 		print_star()
# 	star_count += 1
# 	space_count -=1
# 	loop_count += 1









