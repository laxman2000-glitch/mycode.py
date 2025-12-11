def sort(nums):
   
    for i in range(len(nums)-1):
        m = i
        for j in range(i,len(nums)):
            if nums[j]<nums[m]:
                m = j
                
        temp= nums[i]
        nums[i]=nums[m]
        nums[m]=temp    
        print (nums)  
nums = [9,7,3,6,8,4,2,6,8,1]   
sort(nums)
print(nums)

