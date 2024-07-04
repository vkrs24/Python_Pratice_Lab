#4thJuly2024
#4.Check if element exists in list in Python
#Example

#Input: test_list = [1, 6, 3, 5, 3, 4]
            #3 Check if 3 exist or not.
#Output: True
#Explanation: The output is True because
#the element we are looking is exist in the list.

def exist(arr,ele):
    if ele in arr:
        return True
    else:
       return False

print(exist([1, 6, 3, 5, 3, 4],3))


def exist1(arr,ele):
    for i in arr:
        if(i==ele):
            bool=True
            break
        else:
            bool=False
    return bool

print(exist1([1, 6, 3, 5, 3, 4],7))
