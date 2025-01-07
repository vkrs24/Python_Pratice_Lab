#1July2024
#3.Python Program for Array Rotation (Left)
#Input: Original array: [1, 2, 3, 4, 5, 6, 7, 8]
#Output: Rotated array:  [2, 3, 4, 5, 6, 7, 8, 1]

def array_rotation(arr):
    temp=arr[0]
    for i in range(0,len(arr)-1):   
        arr[i]=arr[i+1]
    arr[-1]=temp
    return arr

print(array_rotation([1, 2, 3, 4, 5, 6, 7, 8]))
