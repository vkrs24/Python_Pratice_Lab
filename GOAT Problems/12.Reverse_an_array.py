def reverse(arr):
    l=len(arr)-1
    for i in range(len(arr)//2):
        arr[i],arr[l-i]=arr[l-i],arr[i]

    print(arr)

reverse([1,2,3,4,5])
reverse(['a','b','c'])
