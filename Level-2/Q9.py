def Index_error(l1,b):
    try:
        a = l1[b]
        return "element is in index"
    except IndexError:
        return "index out of bound"

print(Index_error([1,2,3,4,5],4))