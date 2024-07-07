#7thJuly2024
#14.Python program to print odd numbers in a List

#Example:

#Input: list1 = [2, 7, 5, 64, 14]
#Output: [7, 5]

#Input: list2 = [12, 14, 95, 3, 73]
#Output: [95, 3, 73]

def print_odd_numbers_in_list(arr):
    lst=[]
    for i in range(0,len(arr)):
        if(arr[i]%2!=0):
            lst.append(arr[i])

    return lst

print(print_odd_numbers_in_list([2, 7, 5, 64, 14]))
print(print_odd_numbers_in_list([12, 14, 95, 3 ,73]))

