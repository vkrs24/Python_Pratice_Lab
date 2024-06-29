#27June2025
#Basic Programs
#9.Python Program to Check Prime Number
#Given a positive integer N, The task is to write a Python program to check if the number is Prime or not in Python.
#Examples: 
#Input:  n = 11
#Output: True
#Input:  n = 1
#Output: False
#Explanation: A prime number is a natural number greater than 1 that
#has no positive divisors other than 1 and itself.
#The first few prime numbers are {2, 3, 5, 7, 11, ….}.

def prime(num):
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
Number = int(input("Enter the Number: "))
print(prime(Number))

