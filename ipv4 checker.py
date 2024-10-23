inputt = '100.100.1.1'
store = []
temp =''
status = 0
if len(inputt) > 15 or len(inputt) < 7 or inputt.count('.') != 3:
    print('invalid ipv4 address')
    exit()
else:
    for i in range(len(inputt)):
        if inputt[i] == '.':
            store.append(temp)
            store.append('.')
            temp = ''
        elif inputt[i].isnumeric():
            temp = temp + inputt[i]
            if i == len(inputt)-1:
                store.append(temp)
for i in store:
    if len(i) > 1 and i[0] == '0':
       status = 0
       break
    elif i == '.' or (i.isnumeric() and len(i) <= 3 and int(i) <= 255):
        status += 1
    else:
        status = 0
        break
if status == 7:
    print('valid ipv4 address')
else:
    print('invalid ipv4 address')