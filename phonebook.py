# import stuff 
import os

phonebook_data = [
    {
        "name": "Melissa",
        "number": "404-235-5428"
    },
    {
        "name": "Joe",
        "number": "404-235-2125"
    },
    {
        "name": "Mike",
        "number": "770-134-2229"
    },
    {
        "name": "Igor",
        "number": "770-233-3461"
    }
]

#Main loop 
while 1: 
	print """Electronic Phone Book
	=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Search for an entry
6. Quit
	"""
	user_input = raw_input("What do you want to do (1-6)?")
	# raw_input comes in as what data type? -- string! What are we expecting? int
	# option 2
	try:
		convert_user = int(user_input)
	except ValueError:
		os.system("clear")
		print "You must enter a number!\n"
	else:
		# I tried to convert it and succeeded!
		if(convert_user == 1):
			search = raw_input("Enter a Name: ").capitalize()
			for entry in phonebook_data:
				if search == entry["name"]:
					print entry["number"]
		
		if(convert_user == 2):
			user_prompt = raw_input("Enter Name:").capitalize()
			user_prompt_number = raw_input("Enter Number:")
			# formatted_number = format(int(user_prompt_number[:-1], ",").replace("," "-") + user_prompt_number[-1]
			phonebook_data.append({"name": user_prompt, "number": user_prompt_number})
			print phonebook_data
		
		if(convert_user == 3):
			user_prompt_delete_name = raw_input("Enter Name:").capitalize()
			for entry in phonebook_data:
				if user_prompt_delete_name == entry["name"]:
					phonebook_data.remove(entry)
					print phonebook_data

		if(convert_user == 4):
			print phonebook_data

		if (convert_user == 5):
			find = raw_input("Who are you looking for?").capitalize()
			for entry in phonebook_data:
				if find == entry["name"]:
					print entry


		elif(convert_user == 6):
		#  user chose to quit, exit the loop 
			break