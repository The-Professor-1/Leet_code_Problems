nums = [1,2,3,4]
target = 5
if nums.count(target) == 0:
    nums.append(target)
    nums.sort()
    print(nums.index(target))
else:
    print(nums.index(target))
