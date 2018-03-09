for count in range(1, 1000): #Prints all odd numbers from 1 to 1000
	if count % 2 != 0:
		print count

for count in range(5, 1000000): #Prints all multiples of 5 from 5 to 1,000,000
	if count % 5 == 0:
		print count

a = [1, 2, 5, 10, 255, 3]
sum = 0
for count in range(0, len(a)): #Finds the sum of all numbers in a list
	sum += a[count]
print "Sum: " + str(sum) #Prints the sum
print "Average: " + str(sum / len(a)) #Prints the average of all numbers in a list