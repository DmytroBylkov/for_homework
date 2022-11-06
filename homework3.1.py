def center_of_string(string: str) -> str:
    len_of_string = len(string)
    for_output_center_of_string = len_of_string // 2
    if len_of_string == 0:
        print("")
    elif len_of_string % 2:
        print(string[for_output_center_of_string])
    else:
        print(string[for_output_center_of_string - 1 : for_output_center_of_string + 1])

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
string3 = input("Enter third string: ")

center_of_string(string1)
center_of_string(string2)
center_of_string(string3)

    
