# This code returns the even count of a list
def even_count(list):
    count = 0
    for num in list :
        if num%2 ==0 :
            count+=1
    return count 

list =[2,4,6,8,10,12,14,16,17]
print("Total even number in the list:",even_count(list))