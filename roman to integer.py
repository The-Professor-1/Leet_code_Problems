s = "MMMCDXC"
key = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
sum = 0
for i in range(len(s)):
    if s[i] in key.keys():
        if i != 0 and s[i] == 'M' and s[i-1] == 'C':
            sum = sum + 800
        elif i != 0 and s[i] == 'D' and s[i - 1] == 'C':
            sum = sum + 300
        elif i != 0 and s[i] == 'V' and s[i - 1] == 'I':
            sum = sum + 3
        elif i != 0 and s[i] == 'X' and s[i - 1] == 'I':
            sum = sum + 8
        elif i != 0 and s[i] == 'C' and s[i - 1] == 'X':
            sum = sum + 80
        elif i != 0 and s[i] == 'L' and s[i - 1] == 'X':
            sum = sum + 30
        else:
            sum = sum + int(key[s[i]])
print(sum)