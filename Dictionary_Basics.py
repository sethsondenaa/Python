user = {}

user['name'] = 'Seth'
user['age'] = 23
user['country of birth'] = 'United States of America'
user['favorite language'] = 'Python'

def printDictionary(participant):
	print "My name is " + participant['name']
	print "My age is " + str(participant['age'])
	print "My country of birth is " + participant['country of birth']
	print "My favorite language is " + participant['favorite language']

printDictionary(user)