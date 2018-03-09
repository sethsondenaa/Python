# Write a program that, given some value, tests that value for its type.
# If the value is an integer:
#         If it is greater than or equal to 100 print "That's a big number!"
#         If it is less than 100 print "That's a small number"
# If the value is a string:
#         If the string is greater than or equal to 50 characters print "Long sentence."
#         If the string is shorter than 50 characters print "Short sentence."
#If the value is a list:
#		  If the length is greater than or equal to 10 print "Big list!"
#   	  If it has fewer than 10 values print "Short list."

#Test values
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# Function that tests the size of an integer, string, or list
def test_value(value):
	if isinstance(value, int):
		if value >= 100:
			print "That's a big number!"  # Prints if integer is 100 or larger
		else:
			print "That's a small number." # Prints if integer is less than 100
	elif isinstance(value, str):
		if len(value) >= 50:
			print "Big sentence."    # Prints if string is 50 characters or longer
		else:
			print "Small sentence." #   Prints if string is shorter than 50 characters
	elif isinstance(value, list):
		if len(value) >= 10:
			print "Big list!" # Prints if list has 10 or more values
		else:
			print "Small list." # Prints if list has less than 10 values
	else:
		print "Please enter a value that is either an integer, string, or list." # Request either an interger, string, or list


test_value(eL) # Runs function to test the value given
