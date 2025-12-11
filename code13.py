m= int(input("marks in maths"))
s= int(input("marks in science"))
e= int(input("marks in english"))
s= m+s+e
s2=s/3
p= (s/300)*100
grade =""
if p ==100: 
    grade = "A"
elif p >90:
    grade = "B"
elif  p >=80:
    grade = "C"
elif  p >=70:
    grade = "E"
else:
    grade = "F"
print (f"Total marks:{s}\nAvarage Marks:{p}\nGrade:{grade}")

