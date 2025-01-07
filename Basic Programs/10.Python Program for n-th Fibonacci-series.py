#28June2025
#Basic Programs
#10.Python Program for n-th Fibonacci-series
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
#Fn = Fn-1 + Fn-2
#With seed values 
#F0 = 0 and F1 = 1.
#Input:
#10
#Output:
#0 1 1 2 3 5 8 13 21 34 
#Input:
#9
#Output:
#0 1 1 2 3 5 8 13 21 

def fibonacci(num):
    first=0
    second=1
    string=''
    for i in range(num):
        string +=str(first)+" "
        result=first+second
        second=first
        first=result
    return string
    
Number=int(input("Enter the Number: "))
print(fibonacci(Number))
