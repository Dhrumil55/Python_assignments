def anagram(str1,str2):
    if list(str1).sort() == list(str2).sort():
        return True
a = anagram("listen","silent")
print(a)