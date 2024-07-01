#1July2024
#4.Python Program for Reversal algorithm for array rotation
#Input: Original array: arr[] = [1, 2, 3, 4, 5, 6, 7] d = 2
#Output: Rotated array:  arr[] = [3, 4, 5, 6, 7, 1, 2]

def array_rotation(arr,time):
    for j in range(time):
        temp=arr[0]
        for i in range(0,len(arr)-1):   
            arr[i]=arr[i+1]
        arr[-1]=temp
    return arr

print(array_rotation([1, 2, 3, 4, 5, 6, 7, 8],2))
