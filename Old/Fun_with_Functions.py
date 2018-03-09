a = [2,4,10,16]

#This function prints numbers from 1 to 2000 and is the number is odd or even.
def odd_even():
	output = ""
	for number in range(1, 2001):
		if(number % 2 == 0):
			output = "Number is " + str(number) + ". This is an even number."
		else:
			output = "Number is " + str(number) + ". This is an odd number."
		print output

#This function creates a new list by multiplying all numbers in a given list by a given number and adding them to the new list.
def multiply(inputList, x):
	b = []
	for item in range(0, len(inputList)):
		b.append(inputList[item] * x)
	return b

def layered_multiples(arr):
	new_array = []
	for number in range(0, len(arr)):
		item_array = []
		for multiple in range(0, arr[number]):
			item_array.append(1)
		new_array.append(item_array)
	return new_array	


#odd_even()
#multiply(a, 5)
print multiply([2,4,5],3)
x = layered_multiples(multiply([2,4,5],3))
print x