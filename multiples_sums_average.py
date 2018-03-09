# Multiples
# Part I
# Write code that prints all the odd numbers from 1 to 1000. (Use a for loop and don't use a list for this exercise.)

for odds in range(1, 1001):
	if odds % 2 == 1:
		print odds

# Part II
# Write code that prints all the multiples of 5 from 5 to 1,000,000

for fives in range(5, 1000001):
	if fives % 5 == 0:
		print fives

# Sum List
# Create a program that prints the sum of all values in a list.

a = [1,2,5,10,255,3]

sum = 0
for value in a:
	sum += value

print sum

# Average list
# Create a program that prints the average of the values in a list.

a = [1,2,5,10,255,3]

sum = 0
for value in a:
	sum += value

#Divide the sum by the length of the list.
print sum / len(a)




