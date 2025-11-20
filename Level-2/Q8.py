def vowels(a):
    b = ['a','e','i','o','u']
    c = 0
    for i in a:
        if i in b:
            c+=1
    return c
print(vowels("Hello, World!"))
            
            