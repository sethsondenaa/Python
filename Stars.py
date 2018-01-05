x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

''' This is the function that prints stars from a list of integers
def draw_stars(arr):
	for num in range(0, len(arr)):
		line = ""
		for number in range(0, arr[num]):
			line += "*"
		print line

drawStars(x)
'''

def draw_stars(arr):
	for item in range(0, len(arr)):
		line = ""
		if(isinstance(arr[item], int)):
			for number in range(0, arr[item]):
				line += "*"
			print line
		elif(isinstance(arr[item], str)):
			for number in range(0, len(arr[item])):
				line += arr[item][0].lower()
			print line
		else:
			print "Please enter a list that contains only intergers or strings."

draw_stars(y)




