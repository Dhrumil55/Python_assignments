def pair(l,k):
    l.sort()
    pair_count = 0
    i = 0
    j = len(l)-1
    while i < j:
        if l[i] + l[j] == k:
            pair_count+=1
            i+=1
            j-=1
        elif l[i] + l[j] < k:
            i+=1
        else:
            j-=1
    return pair_count

print(pair([1,2,3,4,5],6))


