def mini(arr):
    index=0
    minimum=arr[0]
    for i in range(0,len(arr)):
        if(minimum>arr[index]):
            minimum=arr[index]
        index+=1
    print(minimum)

mini([1,2,3,4,5])
mini([12,21,13,4,15])
mini([112,2,23,14,15])
mini([11,22,41,42,5])
