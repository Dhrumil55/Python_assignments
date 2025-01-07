def calculate(s:str):
    number = 0
    alphabet = 0
    for i in s:
        if i.isalpha():
            alphabet +=1
        elif i.isdigit():
            number+=1
    return f"Total alphabets: {alphabet}, Total numbers: {number}"

a = calculate("Hello1234")
print(a)            