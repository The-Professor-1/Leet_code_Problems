nums = [1,2,3,3,4,4,5,5,5,6,6]
pair = {}
for i in nums:
    pair.update({nums.count(i):i})
print(pair.get(max( pair.keys())))