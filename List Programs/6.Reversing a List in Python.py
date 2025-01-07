#5thJuly2024
#6.Reversing a List in Python
# Example: 

# Input: list = [4, 5, 6, 7, 8, 9]

# Output: [9, 8, 7, 6, 5, 4]

# Explanation: The list we are having in the output is reversed to the
# list we have in the input.

def Reversing_a_List(arr):
    arr1 = []
    for i in range(len(arr)-1, -1, -1):
        arr1.append(arr[i])
    return arr1

print(Reversing_a_List([4, 5, 6, 7, 8, 9]))

def Reversing_a_List1(arr):
    return arr[::-1]

print(Reversing_a_List1([4, 5, 6, 7, 8, 9]))
