# Write a program that compares two lists. Print "The lists are the same." if they are identical
# Print "The lists are not the same." if they are not identical

def compare_lists(first, second):
	if len(first) != len(second):
		return "The lists are not the same."

	for index in range(0, len(first)):
		if first[index] != second[index]:
			return "The lists are not the same."

	return "The lists are the same"


list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

print compare_lists(list_one, list_two)