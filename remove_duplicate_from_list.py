numbers= [1,1,2,2,3,3,4,5,5,6,7,7,8,9,9,10,10,10]
'''
#Using set() function
unique_numbers = list(set(numbers))
print("Unique Values:",unique_numbers)
'''
'''
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)
'''
unique_numbers = []
for item in numbers:
    if item not in unique_numbers:
        unique_numbers.append(item)
print("Unique Values:",unique_numbers)
