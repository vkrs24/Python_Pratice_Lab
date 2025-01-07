#7thJuly2024
#12.Python program to find N largest elements from a list

#Examples :

#Input : [4, 5, 1, 2, 9] 
        #N = 2
#Output :  [9, 5]

#Input : [81, 52, 45, 10, 3, 2, 96] 
        #N = 3
#Output : [81, 96, 52]

def find_largest_elements_from_list(arr,n):
    lst=[]
    arr=list(set(arr))
    for i in range(n):
        large=arr[0]
        for index in range(1,len(arr)):
            if(large<arr[index]):
                large=arr[index]
        lst.append(large)
        arr.remove(large)
    return lst

print(find_largest_elements_from_list([4, 5, 1, 2, 9],2))
print("\n")
print(find_largest_elements_from_list([81, 52, 45, 10, 3, 2, 96],3))
print("\n")

def find_largest_elements_from_list1(arr,n):
    arr=list(set(arr))
    arr.sort()
    arr.reverse()
    return arr[0:n]

print(find_largest_elements_from_list1([81, 52, 45, 10, 3, 2, 96],3))
print("\n")
print(find_largest_elements_from_list1([4, 5, 1, 2, 9],2))
