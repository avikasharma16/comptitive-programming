n = 5  

for i in range(n):
    hyphens = '-' * i
    stars = ' '.join(['*'] * (n - i))
    print(hyphens+stars) 
