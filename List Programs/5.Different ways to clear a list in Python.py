#4thJuly2024
#5.Different ways to clear a list in Python
#Example

#Input: [2, 3, 5, 6, 7]
#Output: []
#Explanation: Python list is cleared and
#it becomes empty so we have returned empty list.


def clear(arr):
    arr.clear()
    return arr

print(clear([2, 3, 5, 6, 7]))

def clear1(arr):
    arr*=0
    return arr

print(clear1([2, 3, 5, 6, 7]))

def clear2(arr):
    arr=[]
    return arr

print(clear2([2, 3, 5, 6, 7]))

def clear3(arr):
    while(len(arr)!=0):
        arr.pop()
    return arr

print(clear3([2, 3, 5, 6, 7]))

