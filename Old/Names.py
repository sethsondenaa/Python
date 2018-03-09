students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#This functions prints the title of the lists and the lists: number, names, and number of letters in the name. (Use dictionary format of dictionary users above)
def printClass(participants):
	for key in participants:
		print key
		for person in range(0, len(participants[key])):
			print str(person + 1) + " - " + participants[key][person]['first_name'].upper() + " " + participants[key][person]['last_name'].upper() + " - " + str(len(participants[key][person]['first_name'].upper() + participants[key][person]['last_name'].upper()))


#This function prints first and last names from a dictionary. (Use format of students list above.)
def printNames(people): 
	for person in range(0, len(people)):
		print people[person]['first_name'] + " " + people[person]['last_name']

printNames(students)
print " "
printClass(users)