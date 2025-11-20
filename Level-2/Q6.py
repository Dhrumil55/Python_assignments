def power_of_two(num):
    if num/2 == 1:
        return "number is a power of 2"
    elif num/2 < 1:
        return "number is not a power of 2"
    elif num/2 != 1:
        a = num/2
        return power_of_two(a)

print(power_of_two(67))