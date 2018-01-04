import random

tosses = 5000

def coinToss(toss):
	attempt = 0
	heads = 0
	tails = 0
	print "Starting the Program..."
	for flips in range(0, toss):
		attempt += 1
		result = round(random.random())
		if(result == 0):
			tails += 1
			print "Attempt #" + str(attempt) + ": It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
		else:
			heads += 1
			print "Attempt #" + str(attempt) + ": It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
	print "Ending the program. thank you!"


coinToss(tosses)