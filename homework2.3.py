from plistlib import FMT_BINARY


number1 = int(input("Enter first number for fizz: "))
number2 = int(input("Enter second number for buzz: "))
number3 = int(input("Enter a third number for the amount of numbers in the row: "))


for number in range(1, number3 + 1):
    if not number % number1 and not number % number2:
        number = "FB"
        print(number, end=" ")   
    elif not number % number1 and number % number2:
        number = "F"
        print(number, end=" ")
    elif number % number1 and not number % number2:
        number = "B"
        print(number, end=" ")
    else:
         print(number, end=" ")
    
