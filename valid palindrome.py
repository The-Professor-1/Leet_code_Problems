s ='A man, a plan, a canal: Panama'
temp = ''
for i in s:
    if i.isalnum():
        temp = temp + i.lower()
if temp == temp[::-1]:
    print('true')
else:
    print('false')