def specific_sorting_list(list:list)->list:
	list_sort = sorted(list, key=lambda x = list[:5])
	return list_sort


list_for_training = [2, 34, 54, 76, 1, 9, 76, 56, 3, 88, 32, 79, 55, 23, 68, 4, 89, 45, 7, 99, 12, 15, 47]

print(specific_sorting_list(list_for_training))
list = specific_sorting_list(list_for_training)
print(list)
