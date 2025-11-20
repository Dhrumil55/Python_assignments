a = list(input("insert your list: "))
k = int(input("enter the number for right shift: "))
b = []
c = len(a)-1
for i in range(c,c-k,-1):
    b.append(a[i])
    a.pop(i)
b.sort()
a = b + a
print(a)