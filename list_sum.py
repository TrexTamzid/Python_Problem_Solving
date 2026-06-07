#This code returns the total of a given list elements in iterative way.
def sum_of_list(list):
    sum = 0
    for num in list :
        sum += num
    return sum

list = [11,12,13,22,24,23,25,26,14]
print("Total of the list elements:",sum_of_list(list))