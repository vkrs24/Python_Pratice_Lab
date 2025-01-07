def swap(pos1,pos2,arr):
    arr[pos1-1],arr[pos2-1]=arr[pos2-1],arr[pos1-1]
    print(arr)

swap(1,2,[1,2,3,4,5])
swap(2,4,[1,2,3,4,5,6,7])
