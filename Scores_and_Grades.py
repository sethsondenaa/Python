import random
numberOfStudents = 10

def grades(students):
	score = random.randint(60, 100)
	print "Scores and Grades"
	for times in range(0, students):
		if(score >= 60 and score < 70):
			print "Score: " + str(score) + "; Your grade is D"
		elif(score >= 70 and score < 80):
			print "Score: " + str(score) + "; Your grade is C"
		elif(score >= 80 and score < 90):
			print "Score: " + str(score) + "; Your grade is B"
		else:
			print "Score: " + str(score) + "; Your grade is A"
		score = random.randint(60, 100)
	print "End of Program. Bye!"

grades(numberOfStudents)

