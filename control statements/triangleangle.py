angle1=int(input("enter first angle:"))
angle2=int(input("enter second angle:"))
angle3=int(input("enter third angle:"))

if(angle1 == 180 or angle2 ==90 or angle3 == 90):
    print("the angle1 is right angle")
elif(angle2>=90):
    print("the angle2 is obtuse angle")
else:
    print("the angle3 is acute angle")    