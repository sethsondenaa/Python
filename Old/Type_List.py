#l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
#l = ['magical','unicorns']
#l = [bool]

listType = ""
output = ""

for count in range(1, len(l)):
	if(type(l[count]) != type(l[count - 1])):
		listType = "mixed type"
		break

if(listType != "mixed type" and isinstance(l[0], str)):
	listType = "string type"
elif(listType != "mixed type" and isinstance(l[0], int)):
	listType = "integer type"

if(listType == "mixed type"):
	strings = "String:"
	output = "Sum: "
	sum = 0
	for count in range(0, len(l)):
		if(isinstance(l[count], str)):
			strings += " " + l[count]
		elif(isinstance(l[count], int) or isinstance(l[count], float)):
			sum += l[count]
	output += str(sum) 
	print "The list you entered is of " + listType
	print strings
	print output
elif(listType == "string type"):
	output = "String:" 
	for count in range(0, len(l)):
		output += " " + l[count]
	print "The list you entered is of " + listType
	print output
elif(listType == "integer type"):
	output = "Sum: "
	sum = 0
	for count in range(0, len(l)):
		sum += l[count]
	output += str(sum)
	print "The list you entered is of " + listType
	print output
else:
	print "PLease enter a list contains strings, integers, floats, or any combination of the three types."





