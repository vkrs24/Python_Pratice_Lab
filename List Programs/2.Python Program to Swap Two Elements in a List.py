#4thJuly2024
#2.Python Program to Swap Two Elements in a List
#Given a list in Python and provided the positions of the elements,
#write a program to swap the two elements in the list. 

#Examples:  

#Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
#Output : [19, 65, 23, 90]

#Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
#Output : [1, 5, 3, 4, 2]

def swap(arr,pos1,pos2):
    temp=arr[pos1]
    arr[pos1]=arr[pos2]
    arr[pos2]=temp
    return arr

print(swap([23, 65, 19, 90],1-1,3-1))
print(swap([1, 2, 3, 4, 5],2-1,5-1))
