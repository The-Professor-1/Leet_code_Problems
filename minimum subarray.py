nums = [1,2,3,4,5,6]
target = 6
lenlist = []
window = []
start = 0
end = start + 1
sum = 0
index = 0
while(index == 0):
    for i in nums:
        if i >= target:
            lenlist.append(1)
            break
    if window == []:
        window.append(nums[start])
        window.append(nums[end])
    else:
        for i in window:
            sum = sum + i
        if sum >= target:
            lenlist.append(len(window))
            window.clear()
            start += 1
            end = start + 1
        elif end == len(nums)-1 and sum < target:
            print('0')
            index = 1
        else:
            sum = 0
            end += 1
            window.append(nums[end])
            print(window)
print(lenlist)