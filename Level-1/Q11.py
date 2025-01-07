def calculate(num):
    b = 0
    a = str(num)
    if num < 10:
        return num
    for i in a:
        b = b + int(i)
    return calculate(b)
c = calculate(987)
print(c)
        