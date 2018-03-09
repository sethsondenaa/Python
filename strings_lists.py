## Use only built in methods to complete the following exercises:

## 1. Find and Replace
##    Given the string words print the postion of the first instance of the word day. Then
##    Create a new string where the word "day" is replaced with the word month.

words = "It's thanksgiving day. It's my birthday, too!"

print "First instance of the word day: " + str(words.find("day"))
words2 = words.replace("day", "month")
print words2

## 2. Min and Max
##	  Print the min and max in a list of intergers.

x = [2,54,-2,7,12,98]

print "Min: " + str(min(x)) + ", Max: " + str(max(x))

## 3. First and Last
##    Print the first and last values of a list.

x = ["hello",2,54,-2,7,12,98,"world"]
x2 = ["hello","world"]
x3 = ["hello"]

print "First Value: '" + str(x[0]) + "', Last Value: '" + str(x[len(x) - 1]) + "'"
print "First Value: '" + str(x2[0]) + "', Last Value: '" + str(x2[len(x2) - 1]) + "'"
print "First Value: '" + str(x3[0]) + "', Last Value: '" + str(x3[len(x3) - 1]) + "'"

## 4. New List 
##    Split a list and push the first half into postion 0 of the list created from the second half.

##Given list
x = [19,2,54,-2,7,12,98,32,10,-3,6]

## Sorts the given list and sets a new list equal to the sorted given list
x.sort()
new_list = x

## creates a holder list for the second half
second_half = []
count = len(x) - 1
for value in new_list:
	entry = new_list.pop()
	second_half.append(entry)
	count -= 1
	## Breaks the loop when half the list has been removed.
	if count == (len(x) - 1) / 2:
		break

## Sets the first half list into postion 0 of the new list
first_half = new_list
new_list = []
new_list.append(first_half)

## Appends all values in second half list until all are placed into the new list
while len(second_half) != 0:
	new_list.append(second_half.pop())

print new_list




