haystack = "sadbutsad"
needle = 'adb'
start = 0
end = len(needle)
window = []
for j in range(len(haystack)):
    if len(needle)>len(haystack):
        print("not")
        break
    else:
        for i in range(start,end):
            window.append(haystack[i])
    if window == list(needle):
        print(start)
        break
    elif end >= len(haystack) and window != needle:
        print("not found")
        break
    else:
        window.clear()
        start += 1
        end += 1