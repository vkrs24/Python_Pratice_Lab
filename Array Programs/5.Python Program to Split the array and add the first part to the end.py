#1July2024
#5.Python Program to Split the array and add the first part to the end
#Input : arr[] = {12, 10, 5, 6, 52, 36}
#            k = 2
#Output : arr[] = {5, 6, 52, 36, 12, 10}
#Explanation : Split from index 2 and first 
#part {12, 10} add to the end .
#Input : arr[] = {3, 1, 2}
#          k = 1
#Output : arr[] = {1, 2, 3}
#Explanation : Split from index 1 and first
#part add to the end.

def array_split_and_add(arr,index):
    array=arr[index:]+arr[:index]
    return array

print(array_split_and_add([12, 10, 5, 6, 52, 36],2))
