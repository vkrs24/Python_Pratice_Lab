#4thJuly2024
#1.Python program to interchange first and last elements in a list
#Given a list, write a Python program to swap first and last element of
#the list.

#Examples: 

#Input : [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]
#Input : [1, 2, 3]
#Output : [3, 2, 1]

#Approach #1: Find the length of the list and simply swap the first
#element with (n-1)th element.

def interchange(arr):
    temp=arr[0]
    arr[0]=arr[-1]
    arr[-1]=temp
    return arr

print(interchange([12, 35, 9, 56, 24]))
print(interchange([1, 2, 3]))
