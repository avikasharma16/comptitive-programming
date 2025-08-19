num = int(input("Enter a number: "))

if num % 3 == 0 or num % 10 == 4:
    print("The number is either divisible by 3 or its last digit is 4.")
else:
    print("Neither condition is satisfied.")
