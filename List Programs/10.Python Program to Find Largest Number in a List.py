#5thJuly2024
#10.Python Program to Find Largest Number in a List

# Given a list of numbers, the task is to write a Python program to find the largest number in given list. 

# Examples:

# Input : list1 = [10, 20, 4]
# Output : 20


def Largest_number_in_a_list(arr):
    large=arr[0]
    for i in range(0,len(arr)):
        if(large>arr[i]):
            continue
        else:
            large=arr[i]
    return large

print(Largest_number_in_a_list([10, 20, 4]))
print(Largest_number_in_a_list([20, 10, 20, 1, 100]))

