nums = [-1,0,0,0,0,3,3]
temp = []
for i in nums:
    if nums.count(i) > 1:
        nums.remove(i)
        if i not in nums:
            nums.append(i)
print(nums)
