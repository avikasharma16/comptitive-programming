n = 5                                 
for i in range(1, n + 1):                    
    for j in range(1, n + 1):
        if (j==1)or(j== n):
            print("*", end="")
        else:
            print ("_", end="") 
    print()

     
#n = 5  

#for i in range(1, n + 1):
 #   print("_" * (n - i), end="")
  #  print("*"*i)

n = int(input("Enter number of underscores in first row: "))

for i in range(n, 0, -1):
    if i == 1:   
        print("_")
    else:
        underscores = "_ " * (i - 1)   
        print("* " + underscores +"*")
