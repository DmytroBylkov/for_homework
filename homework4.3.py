def specific_sorting_list(list:list)->list:
	counter = 0
	new_list =[]
	while len(list)> 0:
		list1 = list[:5]
		if counter % 2:
			list1.sort(reverse=True)
		else:
			list1.sort()
		counter += 1
		list = list[5:]
		new_list.extend(list1)
	return new_list


list_for_training = [2, 34, 54, 76, 1, 9, 76, 56, 3, 88, 32, 79, 55, 23, 68, 4, 89, 45, 7, 99, 12, 15, 47]

print(specific_sorting_list(list_for_training))
