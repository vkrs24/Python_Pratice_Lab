#7thJuly2024
#11.Python program to find second largest number in a list

#Examples: 

#Input: list1 = [10, 20, 4]
#Output: 10

#Input: list2 = [70, 11, 20, 4, 100]
#Output: 70

def second_largest_number_in_a_list(arr):
    large=arr[0]
    cnt=0
    while(cnt!=2):
        for index in range(0,len(arr)):
            if(large<arr[index]):
                large=arr[index]
        cnt+=1
        if(cnt!=2):
            arr.remove(large)
        else:
            return large
        large=arr[0]

print(second_largest_number_in_a_list([70, 11, 20,20, 4, 100]))
print(second_largest_number_in_a_list([10, 20, 4]))

def second_largest_number_in_a_list1(arr):
    arr.sort()
    return arr[-2]

print(second_largest_number_in_a_list1([70, 111, 20,20, 4, 100]))
print(second_largest_number_in_a_list1([10, 20,12,14]))
