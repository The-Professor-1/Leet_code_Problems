t="sadbutsad"
s="adbu"
temp = []
for i in range(len(s)):
    if t.find(s[i]) != -1:
        t=t[t.index(s[i])+1:]
        print(t)
        temp.append((s[i]))
if len(s) == len(temp):
    print('true')
else:
    print('false')
print(temp)