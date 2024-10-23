s = 'what are you talking '
store = []
count = 1
for i in range(len(s)-1,-1,-1):
    if s[i] ==' ' and count == 1:
        continue
    elif s[i] ==' ' and count > 1:
        store.append(count-1)
        count = 1
    elif i == 0 and count > 0:
        store.append(count)
        break
    else:
        count += 1
print(store)