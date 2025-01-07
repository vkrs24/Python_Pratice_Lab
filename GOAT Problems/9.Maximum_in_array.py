def maxi(arr):
    index=0
    maximum=0
    for i in range(0,len(arr)):
        if(maximum<arr[index]):
            maximum=arr[index]
        index+=1
    print(maximum)

maxi([1,2,3,4,5])
maxi([12,21,13,4,15])
maxi([112,21,23,4,15])
maxi([12,22,42,42,15])
