string = 'w3resource' 
dict_1 = {}
for index in string:
    dict_1[index] = dict_1.get(index, 0) + 1
print(dict_1)

