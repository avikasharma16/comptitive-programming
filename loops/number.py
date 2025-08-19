n=int(input("enter a number:"))
digit=0
while(n>0):
    n //= 10
    digit=digit+1
print("number of digits:", digit)    