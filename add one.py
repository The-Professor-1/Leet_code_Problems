num = [1,3,9,9,0]
one =''
for i in range(len(num)):
    one += str(num[i])
summ = int(one) + 1
num.clear()
for i in str(summ):
    num.append(i)
print(num)
