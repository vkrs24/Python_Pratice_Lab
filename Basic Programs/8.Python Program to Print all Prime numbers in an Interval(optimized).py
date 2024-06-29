#27June2025
#Basic Programs
#8.Python Program to Print all Prime numbers in an Interval
#Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.
#Definition: A prime number is a natural number greater than 1 that has no
#positive divisors other than 1 and itself.
#The first few prime numbers are {2, 3, 5, 7, 11, ….}.
#Input:
#starting number: 2
#ending number: 10
#Output:
#2 3 5 7 

def prime(start,end):
    flag=0
    for i in range(start,end):
        if(i==1):
            continue
        else:
            for j in range(2,i):
                if(i%j==0):
                    flag=1
                    break
                else:
                    flag=0
            if(flag==0):
                print(i)

start=int(input("Starting Number: "))
end=int(input("Ending Number: "))
prime(start,end)
