def max_of_list (list):
    max_value = list[0]
    for num in list :
        if num > max_value :
            max_value = num
    return num
list =[12,3,4,14,15,5,6,19]
print("Largets element of the list:",max_of_list(list))
