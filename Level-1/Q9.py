def frequency(input_list):
    #a = list(set(input_list))
    a = {key:input_list.count(key) for key in input_list}
    print(a)
frequency([1, 2, 3, 2, 4, 1, 2, 4, 5])