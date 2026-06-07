# This code returns the reverse of a list using iterative way 
list = [1,2,3,4,5]
reversed_list = []
for i in range(len(list)-1,-1,-1):
    reversed_list.append(list[i])
print("List is reversed:",reversed_list)