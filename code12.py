a=input("give numbers")
x,y,z =a.split(",")
a=int(x)
b=int(y)
c=int(z)
largest=0
if  a>b:
   if a>c:
       largest= a
   else:
       largest= c
elif b>a:
   if b>c:
       largest= b
   else:
       largest= c
elif c>a:
   if c>b:
       largest= c
   else:
       largest= b
print(f"Largest number:{largest}")

