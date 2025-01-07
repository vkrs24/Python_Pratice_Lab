#4thJuly2024
#3.How To Find the Length of a List in Python
#Example:

#Input: lst = [10,20,30,40]
#Output: 4
#Explanation: The output is 4 because the length of the list is  4.

def length_of_list(arr):
    cnt=0
    for i in arr:
        cnt+=1
    return cnt

print(length_of_list([10,20,30,40]))

def length_of_list_1(arr):
    cnt=0
    while(1):
        if(arr[cnt]=='\0'):
            break
        else:
            cnt+=1
    return cnt

print(length_of_list_1([10,20,30,40,'\0']))
