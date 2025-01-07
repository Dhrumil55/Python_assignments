def sum_of_odd(start,end):
    total_sum = 0
    for i in range(start,end):
        if i%2 != 0:
            total_sum += i
    return total_sum

a = sum_of_odd(1,10)
print(a)
        