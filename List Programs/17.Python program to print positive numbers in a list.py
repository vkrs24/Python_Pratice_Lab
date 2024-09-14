#14Sept2024
#17.Python program to print positive numbers in a list

# Input: list1 = [12, -7, 5, 64, -14]
# Output: [12, 5, 64]

# Input: list2 = [12, 14, -95, 3]
# Output: [12, 14, 3]

def positive(arr):
    lst=[]
    for i in arr:
        if(i>0):
            lst.append(i)
    print(lst)


positive([12, -7, 5, 64, -14])
positive([12, 14, -95, 3])