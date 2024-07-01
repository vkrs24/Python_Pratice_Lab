#1July2024
#2.Python Program to Find Largest Element in an Array

#To find the largest element in an array, iterate over each element and
#compare it with the current largest element. If an element is greater,
#update the largest element. At the end of the iteration, the largest
#element will be found.

#Given an array, find the largest element in it.

#Input : arr[] = {10, 20, 4}
#Output : 20
#Input : arr[] = {20, 10, 20, 4, 100}
#Output : 100

def find_largest_number(arr):
    low=0
    for i in range(0,len(arr)):
        if(arr[i]>=low):
            high=arr[i]
            low=high
        else:
            low=arr[i]
    return high

print(find_largest_number([10, 20, 4]))
print(find_largest_number([20, 10, 20, 4, 100]))
