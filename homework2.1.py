number = int(input("Enter number of year: "))

if (not number % 4 and number % 100) or (not number % 400):
    print("Yes") 
else:
    print("NO")