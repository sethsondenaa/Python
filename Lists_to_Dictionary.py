name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

animal = ["wolf", "tiger", "sloth", "rhino", "chickadee"]
area = ["Canada", "India", "South America", "Africa"]

#This function combines two lists into a single dictionary (Uses the longer list as values and shorter list as values)
def make_dict(list1, list2):
	new_dict = {}
	count = 0
	#If list1 is longer or equal to list2 use, list1 as keys and list2 as values
	if(len(list1) >= len(list2)):
		for entry in list1:
			try:
				new_dict[entry] = list2[count]
			except IndexError:
				new_dict[entry] = ""
	  		count += 1
	#If list2 is longer than list1, use list2 as keys and list1 as values
	else:
		for entry in list2:
			try:
				new_dict[entry] = list1[count]
			except IndexError:
				new_dict[entry] = ""
	  		count += 1
	return new_dict

print make_dict(animal, area)