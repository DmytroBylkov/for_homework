number = int(input("Enter number of year: "))

if number % 400 == 0:
    print("YES")
elif number % 4 == 0 and number % 100 != 0:
    print("YES")
else:
    print("NO")
