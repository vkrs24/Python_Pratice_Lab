#7thJuly2024
#13.Python program to print even numbers in a list

#Example: 

#Input: list1 = [2, 7, 5, 64, 14]
#Output: [2, 64, 14]

#Input: list2 = [12, 14, 95, 3]
#Output: [12, 14]

def print_even_numbers_in_list(arr):
    lst=[]
    for i in range(0,len(arr)):
        if(arr[i]%2==0):
            lst.append(arr[i])

    return lst

print(print_even_numbers_in_list([2, 7, 5, 64, 14]))
print(print_even_numbers_in_list([12, 14, 95, 3]))
