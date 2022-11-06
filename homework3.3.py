def mix_string(string: str) -> str:
    len_of_string = len(string)
    if len_of_string < 11 and len_of_string > 6:  
        for_center_of_string = len_of_string // 2
        first_part = string[:-3]
        second_part = string[-3].lower()
        
        if len(first_part) == 0:
            print("second")
        else:
            print(second_half + first_half)

start_string = "manufactura"
mix_string(start_string)


    
