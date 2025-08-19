number = int(input("enter the no:"))
count = 2
sum = 0
while count <= number:
    if count % 2 == 0:
        sum = sum + count
    count = count +1
print(sum) 