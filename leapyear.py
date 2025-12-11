a= int(input("enter a year:"))
leap = False 
if a%100 == 0 and a%400 != 0: 
    leap = False
elif a%4 == 0:
    leap = True
else:
    leap = False
if leap == True:
    print(f"it\'s a leap year")
elif leap == False:
    print("it\'s not a leap year")
