def median(l1):
    a = len(l1)/2
    if a%2 == 0:
        b = round(a)
        m = (l1[b]+l1[b-1])/2
        return m
    elif a%2 != 0:
        b = round(a)
        m = l1[b-1]
        return m
print(median([2, 3, 11, 13, 17, 26, 34]))