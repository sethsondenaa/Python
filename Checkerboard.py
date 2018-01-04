#This builds the rows by square then prints by row
for rows in range(0,8):
	row = ""
	if(rows % 2 == 0):
		for square in range(0,8):
			if(square % 2 == 0):
				row += "*"
			if(square % 2 != 0):
				row += " "
	elif(rows % 2 != 0):
		for square in range(0,8):
			if(square % 2 == 0):
				row += " "
			if(square % 2 != 0):
				row += "*"
	print row

#   This prints the board row by row.
'''
for row in range(0,8):
	if(row % 2 != 0):
		print "* * * * "
	if(row % 2 != 0):
		print " * * * *"
'''