def read_file(filename: str) -> list:
	with open(filename) as file:
		text_from_file = [line.replace("\n", "") for line in file.readlines()]
	return text_from_file

def calculate(list: list) -> list:
	result = [arg for arg in list]
	finall_result_list = []
	for el in result:
		try:
			finall_result = eval(el)
		except ZeroDivisionError:
			finall_result = "ZeroDivisionError"
		finall_result_list.append(finall_result)
	return finall_result_list


def re_write_file(filename: str):
	data_from_file = read_file(filename)
	calculating_data = calculate(data_from_file)
	with open("file_1.txt", "w") as file:
		for index,el in enumerate(data_from_file):
			print(el + " = " + str(calculating_data[index]), file=file)

re_write_file("file_1.txt")