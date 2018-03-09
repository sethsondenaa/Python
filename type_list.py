# Write a program that list and prints a message for each element in the list, based on that element's data type
# Your program will always input a list. 

list1 = ['magical unicorns',19,'hello',98.98,'world']
# Output:
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

list2 = [2,3,1,7,4,12]
# Output:
# "The list you entered is of integer type"
# "Sum: 29"

list3 = ['magical','unicorns']
# Output: 
# "The list you entered is of string type"
# "String: magical unicorns"

list4 = [("Only enter", "str, int, or float")]

list6 = ["Oops!",("Only enter", "str, int, or float")] # Still breaks on this code, mixed with elements that aren't string, interger, or float.

list5 = [1.5,3.25,2.75] # Total = 7.5

def type_list(li):
	mixed = "no"
	# Test if the list is a mixed list
	for entry in range(0, len(li)):
		if type(li[entry]) != type(li[entry - 1]):
			mixed = "yes"
			break

	# Prints string total and number total from a mixed list
	if mixed == "yes":
		line_one = "The list you entered is of mixed type"
		line_two = "String:"
		total = 0
		for entry in li:
			if isinstance(entry, str):
				line_two += " " + entry
			else:
				total += entry
		print line_one
		print line_two
		print "Sum: " + str(total)
	# Prints string total from a string list
	elif isinstance(li[0], str): 
		line_one = "The list you entered is of string type"
		line_two = "String:"
		for entry in li:
			line_two += " " + entry
		print line_one
		print line_two
	# Prints total from an integer list
	elif isinstance(li[0], int):
			line_one = "The list you entered is of integer type"
			total = 0
			for entry in li:
				total += entry
			print line_one
			print "Sum: " + str(total)
	# Prints total from a float list
	elif isinstance(li[0], float):
		line_one = "The list you entered is of float type"
		total = 0
		for entry in li:
			total += entry
		print line_one
		print "Sum: " + str(total)
	else:
		print "Please enter a list that contains only strings, integers, or floats!"


type_list(list4)
