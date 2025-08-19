A = int(input("Enter the base A: "))
B = int(input("Enter the exponent B: "))
i = 1
count = 0
while count < B:
    i *= A
    count += 1
    print(f"{A}^{B} = {i}")
