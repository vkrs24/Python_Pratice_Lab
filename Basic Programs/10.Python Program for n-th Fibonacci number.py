#28June2025
#Basic Programs
#10.Python Program for n-th Fibonacci number
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
#Fn = Fn-1 + Fn-2
#With seed values 
#F0 = 0 and F1 = 1.
#Input:
#10
#Output:
#34
#Input:
#9
#Output:
#21

def fibonacci(num):
    first=0
    second=1
    for i in range(num):
        result=first+second
        second=first
        first=result
    print(second)

Number=int(input("Enter the Number: "))
fibonacci(Number)
