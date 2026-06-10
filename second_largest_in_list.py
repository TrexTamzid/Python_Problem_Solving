#Showing second largest element in a list .
numbers = [13,36,1,9,33,3]
largest = second_largest = float("-inf")

for num in numbers :
    if num > largest :
        second_largest = largest 
        largest = num
    elif largest > num >second_largest :
        second_largest = num

print("Second Largest Element:",second_largest)