# 14Sept2024
# 18.python program to print negative numbers in a list

# Input: list1 = [12, -7, 5, 64, -14]
# Output: -7, -14

# Input: list2 = [12, 14, -95, 3]
# Output: -95

def negative(arr):
    lst=[]
    for i in arr:
        if(i<0):
            lst.append(i)
    print(lst)

negative([12, -7, 5, 64, -14])
negative([12, 14, -95, 3])