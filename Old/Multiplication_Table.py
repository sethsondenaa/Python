line = "x"
for col in range(1, 13): #Sets up first row
	line += " " + str(col)
print line #Prints first row

for col in range(1, 13):
	line = str(col) + " "
	for  row in range(1, 13):
		 line += str(row * col) + " " 
	print line