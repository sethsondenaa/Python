words = "It's thanksgiving day. It's my birthday,too!"
print "First instance of day: " + str(words.find("day")) #Prints the first instance of day in a string
words = words.replace("day", "month") #Replaces all instances of "day" with "month" in a string
print words #Prints the string

x = [2,54,-2,7,12,98]
print "Min: " + str(min(x)) + ", Max: " + str(max(x)) #Prints the Minimum and Maximum of a list

x = ["hello",2,54,-2,7,12,98,"world"]
print "First: " + str(x[0]) + ", Last: " + str(x[len(x)-1]) #Prints the first and last items of a list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort() #Sorts a list
firstHalf = []
for count in range(0, (len(x) / 2)):
	firstHalf.append(x[count])
x2 = [firstHalf]
for count in range((len(x) / 2), len(x)):
	x2.append(x[count])
print x2 #Creates a list with the first entry as the first half of inputed list and the remaining list appeneded after.
