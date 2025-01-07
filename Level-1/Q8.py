def LCM(a,b):
    largest = max(a,b)
    smallest = min(a,b)
    for i in range(largest,(a*b)+1,largest):
        if i % smallest == 0:
            return i
find = LCM(12,18)
print(find)