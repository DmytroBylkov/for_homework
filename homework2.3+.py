from plistlib import FMT_BINARY


number1 = int(input("Enter first number for fizz: "))
number2 = int(input("Enter second number for buzz: "))
number3 = int(input("Enter a third number for the amount of numbers in the row: "))

result_list = []
for number in range(1, number3 + 1):
    if not number % number1 and not number % number2:
        number = "FB"   
    elif not number % number1 and number % number2:
        number = "F"
    elif number % number1 and not number % number2:
        number = "B"
    result_list.append(number)

print(result_list)