def perfect_number(num):
    a = [1]
    for i in range(2,int(num/2)+1):
        if num%i == 0:
            a.append(i)
    if sum(a) == num:
        return f"{num} is a perfect number"

b = perfect_number(6)
print(b)