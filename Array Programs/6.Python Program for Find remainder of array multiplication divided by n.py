#1July2024
#6.Python Program for Find remainder of array multiplication divided by n
#Write a Python program for a given multiple numbers and a number n,
#the task is to print the remainder after multiplying all the numbers
#divided by n.

#Examples:

#Input: arr[] = {100, 10, 5, 25, 35, 14},
#n = 11
#Output: 9
#Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
#Input : arr[] = {100, 10},
#n = 5
#Output : 0
#Explanation: 100 x 10 = 1000 % 5 = 0

def array_multiplication(arr,n):
    array_multiple=1
    for i in range(0,len(arr)):
        array_multiple*=arr[i]
    return array_multiple%n

print(array_multiplication([100, 10, 5, 25, 35, 14],11))
print(array_multiplication([100, 10],5))
