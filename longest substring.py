haystack = "besttimetosellandbuy"
start = 0
end = 1
wordslist = [0]
window = []
if haystack == "":
    print("0")
else:
    window.append(haystack[0])
    while(end < len(haystack)):
        if haystack[end] not in window:
            window.append(haystack[end])
            end += 1
            print(window)
        elif haystack[end] in window:
            if len(window) > max(wordslist):
                wordslist.clear()
                wordslist.append(len(window))
                window.clear()
                start += 1
                end = start + 1
                window.append(haystack[start])
            else:
                window.clear()
                start += 1
                end = start + 1
                window.append(haystack[start])
if len(window) > max(wordslist):
    wordslist.clear()
    wordslist.append(len(window))
print(max(wordslist))

