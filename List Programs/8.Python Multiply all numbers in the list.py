#5thJuly2024
#8.Python | Multiply all numbers in the list

# Given a list, print the value obtained after multiplying all numbers in a Python list. 

# Examples: 

# Input :  list1 = [1, 2, 3]
# Output : 6
# Explanation: 1*2*3=6

# Input : list1 = [3, 2, 4]
# Output : 24

def Multiply_element_in_list(arr):
    product=1
    for i in arr:
        product*=i
    return product

print(Multiply_element_in_list([1, 2, 3]))

def Multiply_element_in_list1(arr):
    product=1
    cnt=0
    while(cnt<len(arr)):
        product*=arr[cnt]
        cnt+=1
    return product

print(Multiply_element_in_list1([3, 2, 4]))
    
