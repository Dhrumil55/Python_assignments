def common_elements(l1,l2):
    a = set(l1)
    b = set(l2)
    c = a & b
    d = list(c)
    return d

e = common_elements([1,2,3,4,5],[4,5,6,7,8])
print(e)