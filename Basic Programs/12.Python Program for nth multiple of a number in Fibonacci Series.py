#29June2025
#Basic Programs
#12.Python Program for nth multiple of a number in Fibonacci Series
#Given two integers n and k. Find position the nth multiple of K in
#the Fibonacci series. 
#Examples:

#Input: k = 2, n = 3
#Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears
#at position 9.

#Input: k = 4, n = 5 
#Output: 30, 5th multiple of 4 in Fibonacci Series is 832040 which
#appears at position 30.

def fibonacci(k,n):
    first=0
    second=1
    nth=0
    position=0
    while(nth<=n):
        if(first%k==0):
            nth+=1
            value=first
            current_position=position
        result=first+second
        second=first
        first=result
        position+=1
    return f"{n}th multiple of {k} in Fibonacci Series is {value} which appears at position {current_position}"

K=int(input("Enter the K: "))
N=int(input("Enter the N: "))
print(fibonacci(K,N))
    
