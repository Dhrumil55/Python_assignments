def reverse(Input_sentence):
    a = Input_sentence.split()
    a.reverse()
    b = str(" ".join(a))
    return b
c = reverse("Hello, World! Welcome to Python programming.")
print(c)
