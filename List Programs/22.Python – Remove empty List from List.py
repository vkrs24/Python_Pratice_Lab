# 14Sept2024
# 22.Python – Remove empty List from List

# Input: The original list is : [5, 6, [], 3, [], [], 9]

# Output: List after empty list removal : [5, 6, 3, 9]

def empty_list(arr):
    lst=[]
    for i in arr:
        if(i!=[]):
            lst.append(i)
    print(lst)

empty_list([5, 6, [], 3, [], [], 9])