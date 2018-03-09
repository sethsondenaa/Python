my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_to_tuple_list(dictionary):
	my_list = []
	for key in dictionary:
		entry = (key, dictionary[key])
		my_list.append(entry)
	return my_list

print dict_to_tuple_list(my_dict)