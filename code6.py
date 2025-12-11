def sum(**b):
    
    
    for i,l in b.items():
        print(i,l)
sum(name='laxman', age=25, mob=9100353842)'''
'''def username(names):
    for i in names:
        if len(i)<=6:
            print(i)
    
#a, b, c = map(int, input("Give numbers: ").split(","))
  
names = input("give names of students").split(",")
username(names)
