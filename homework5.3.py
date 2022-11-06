def is_palindrom(string: str) -> bool:
    string = string.lower()
    string1 = "".join(el for el in string if el.isalnum())
    if len(string1) <= 1:
        return True
    if string1[0] == string1[-1]:
        return is_palindrom(string1[1:-1])
    if string1[0] != string1[-1]:
        return False
    
if __name__ == "__main__":
    string = "І що сало? Ласощі"
    print(is_palindrom(string))
    
