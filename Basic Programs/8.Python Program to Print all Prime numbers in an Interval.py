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
start=int(input("Starting Number: "))
end=int(input("Ending Number: "))
for i in range(start,end+1):    
    if(i==1 or i==0):
        continue
    if(i==2 or i==3 or i==5 or i==7):
        print(i)
    else:
        if(i%2!=0):
            if(i%3!=0 and i%5!=0):
                if(i%7!=0):
                    print(i)
