def sec_max(arr):
    maxi=arr[0];
    s_maxi=0;
    for i in range(1,len(arr)):
        if(arr[i]>maxi):
            s_maxi=maxi
            maxi=arr[i]
        elif(s_maxi<arr[i]):
            s_maxi=arr[i]
    print(arr)
    print(s_maxi)

sec_max([1,2,3,4,5])
sec_max([51,12,32,42,25])
