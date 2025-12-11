def greet(list2):
    list1=list2.copy()
    list1[2]=40
    print(f"list1:{list1}")
    print(f"idlist1:{id(list1)}")
list2 = [10,20,30]
print(f"id(list2:{id(list2)}")
print(f"list2:{list2}")
greet(list2)
