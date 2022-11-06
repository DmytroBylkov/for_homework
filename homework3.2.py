def mix_half_of_string(string: str) -> str:
    len_of_string = len(string)
    if len_of_string > 4 and len_of_string < 16:
        for_center_of_string = len_of_string // 2
        first_half = string[:for_center_of_string]
        second_half = string[for_center_of_string:]
        second_half = second_half[:-3] + second_half[-3:].upper()
        print(second_half + first_half)

start_string = "manufactura"
mix_half_of_string(start_string)


    
