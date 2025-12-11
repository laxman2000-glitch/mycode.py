arr = [5, 9, 12, 18, 21, 27, 33, 40, 52, 60]

n = 40
l = 0
u = len(arr)-1
i = 0
while  l<=u :
    mid = (l+u)//2
    if arr[mid] ==n:
        i = mid
        print("found",i+1)
        i+=1
        break
    else:
        
        if mid != l:
            l = mid+1
        else :
            u = mid-1
            print("notfound")
            break

      
