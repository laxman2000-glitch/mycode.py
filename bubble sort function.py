def names(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp= nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                
nums = [9,7,3,6,8,4,2,6,8,1]   
names(nums)
print(nums)
