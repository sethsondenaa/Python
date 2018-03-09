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

input = mL
#input = 3.5 was tested. A float returns request for integer, string, or list 

if isinstance(input, int):
	if input >= 100:
		print "That's a big number!" #Prints big number for integers greater than or equal 100
	else:
		print "That's a small number" #Prints small number for integers smaller than 100
elif isinstance(input, str):
	if len(input) >= 50:
		print "Long sentence." #Prints long sentence for strings longer than or equal to 50 characters
	else:
		print "Short sentence." #Prints short sentence for strings smaller than 50 characters
elif isinstance(input, list):
	if len(input) >= 10:
		print "Big list!" #Prints big list for lists with 10 or more items
	else:
		print "Short list." #Prints short list for lists with less than ten items.
else:
	print "Please enter an integer, string, or list for this exercise" #Prints request for integer, string, or list input



