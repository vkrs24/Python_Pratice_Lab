#28June2025
#Basic Programs
#11.Python Program for How to check if a given number is Fibonacci number?
#Given a number \’n\’, how to check if n is a Fibonacci number.
#First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, .. 
#Examples : 
#Input: 8
#Output: Yes
#Input: 34
#Output: Yes
#Input: 41
#Output: No
import math
def sqrt(x):
    sqrt_num=int(math.sqrt(x))
    if(pow(sqrt_num,2)==x):
        return True
    else:
        return False

def isperfectsquare(num):
    return sqrt(5*num*num+4) or sqrt(5*num*num-4)

Number=int(input("Enter the Number: "))
print(isperfectsquare(Number))
    
