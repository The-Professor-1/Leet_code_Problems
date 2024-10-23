nums = [0,1,2,2,0,3,4]
val = 2
newnum = []
for i in range(len(nums)-1):
    if nums[i] == val:
        nums.remove(nums[i])
    elif nums[i] != val:
        newnum.append(nums[i])
k = len(newnum)
print(k,newnum,nums)