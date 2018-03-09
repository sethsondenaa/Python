list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

output = "The lists are the same."

for count in range(0, len(list_one)):
	if(len(list_one) != len(list_two)):
		output = "The lists are not the same."
		break
	if(list_one[count] != list_two[count]):
		output = "The lists are not the same."
		break

print output