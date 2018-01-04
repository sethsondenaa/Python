#Checks if number is a Prime number
def isPrime(number): 
	prime = "yes"
	for count in range(2, number / 2):
		if(number % count == 0):
			prime = "no"
			return prime
	return prime

#Checks if number is a Square number
def isSquare(number):
	square = "no"
	for count in range(2, number):
		if(count * count == number):
			square = "yes"
			return square
	return square

'''
This function prints all Prime and Square numbers, within a given range, with a descrtiption. 
	If the number is prime the function prints the number with descrtiption Foo.
	If the number is square the function prints the number with description Bar.
	If  the number is neither the function prints FooBar.
'''
def foobar(start, end):
	for count in range(start, end):
		if(count % 2 != 0 or count == 2):
			if(isPrime(count) == "yes"):
				print str(count) + " Foo "
		elif(isSquare(count) == "yes"):
			print str(count) + " Bar"
		else:
			print "FooBar"

foobar(101, 100001)
