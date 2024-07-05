#5thJuly2024
#7.Python program to find sum of elements in list

# Given a list of numbers, write a Python program to find the sum of all the elements in the list.

# Example:  

# Input: [12, 15, 3, 10]
# Output: 40

# Input: [17, 5, 3, 5]
# Output: 30

def sum_of_list(arr):
    sums=0
    for i in arr:
        sums+=i
    return sums

print(sum_of_list([12, 15, 3, 10]))

def sum_of_list1(arr):
    sums,i=0,0
    while(i<len(arr)):
        sums+=arr[i]
        i+=1
    return sums

print(sum_of_list1([17, 5, 3, 5]))

