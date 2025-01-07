#14Sept2024
#21.Remove Multiple Elements from List in Python

#Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [3, 5, 7]

#Output: [1, 2, 4, 6, 8, 9, 10]

def removes(arr,rmv_arr):
    for i in rmv_arr:
        for j in arr:
            if(i==j):
                arr.remove(i)
    print(arr)

removes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[3, 5, 7])