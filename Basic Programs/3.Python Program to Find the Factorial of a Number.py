#26June2025
#Basic Programs
#3.Python Program to Find the Factorial of a Number
#Input: 5
#Output: Factorial of 5 is 120
#Hint: For example factorial of 6 is 6*5*4*3*2*1 which is 720.

fact_number=int(input("Enter the Number: "))
fact=1
for i in range(fact_number,1,-1):
    fact*=i
print(f'Factorial of {fact_number} is {fact}')
