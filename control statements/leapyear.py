Year = int(input("enter the year:"))
if(Year % 400 == 0 and Year % 100 == 0):
    print("Year is leap Year")
else:
    print("year is not a leap  year")