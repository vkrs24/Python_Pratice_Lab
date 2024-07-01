#1July2024
#7.Python Program to check if given array is Monotonic
#Given an array A containing n integers. The task is to check whether
#the array is Monotonic or not. An array is monotonic if it is either
#monotone increasing or monotone decreasing. An array A is monotone
#increasing if for all i <= j, A[i] <= A[j]. 

#An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. 

#Return Type: Boolean value, “True” if the given array A is monotonic
#else return “False” (without quotes). 

#Examples:

#Input : 6 5 4 4
#Output : true

#Input : 5 15 20 10
#Output : false

def assend(arr):
    for i in range(0,len(arr)-1):
        if(arr[i]<=arr[i+1]):
            bool=True
        else:
            bool=False
            break
    return bool

def desend(arr):
    for i in range(0,len(arr)-1):
        if(arr[i]>=arr[i+1]):
            bool=True
        else:
            bool=False
            break
    return bool

def array_monotonic(arr):
    if(arr[0]<=arr[1]):
        return assend(arr)
    else:
        return desend(arr)

print(array_monotonic([6, 5, 4, 4]))
print(array_monotonic([5, 15, 20, 10]))
print(array_monotonic([1, 2, 3, 4, 5]))
print(array_monotonic([5, 4, 3, 2, 1]))
print(array_monotonic([1, 2, 2, 3, 4]))
print(array_monotonic([1, 2, 3, 4, 5, 4]))
# True
# False
# True
# True
# True
# False




