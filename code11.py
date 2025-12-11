from array import*
arr = array('i',[])
m = int(input("give the total number of values"))
for i in range (m):
    x = int(input("give the number"))
    arr.append(x)

print(arr)
val = int(input("give the number for index"))
k=0
for e in arr:
    if val==e:
        print(k)
        break
    k+=1
else:
    print("give correct index value")
index = int(input("Enter index number: "))

if 0 <= index < len(arr):
    print("Value at that index:", arr[index])
else:
    print("Invalid index")
print("bye")
