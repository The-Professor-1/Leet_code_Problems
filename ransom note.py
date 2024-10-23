ransomNote = "babaa"
magazine = "aab"
count = len(ransomNote)
for i in ransomNote:
    if i in magazine:
        list(magazine).pop(magazine.index(i))
        count -= 1
if count == 0:
    print('true')
else:
    print('false')