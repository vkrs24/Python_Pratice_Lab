#5thJuly2024
#9.Python program to find smallest number in a list

# Example: 

# Input : list1 = [10, 20, 4]
# Output : 4

# Input : list2 = [20, 10, 20, 1, 100]
# Output : 1

def smallest_number_in_a_list(arr):
    small=arr[0]
    for i in range(0,len(arr)):
        if(small<arr[i]):
            continue
        else:
            small=arr[i]
    return small

print(smallest_number_in_a_list([10, 20, 4]))
print(smallest_number_in_a_list([20, 10, 20, 1, 100]))
