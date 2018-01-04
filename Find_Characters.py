word_list = ['hello','world','my','name','is','Anna']
char = 'o'

new_list = []

for count in range(0, len(word_list)):
	if char in word_list[count]:
		new_list.append(word_list[count])

print "New_List = " + str(new_list)
