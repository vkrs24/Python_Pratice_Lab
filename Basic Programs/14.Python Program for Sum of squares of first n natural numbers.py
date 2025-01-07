#29June2025
#Basic Programs
#14.Python Program for Sum of squares of first n natural numbers

#Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2. 

#Examples:

#Input : N = 4
#Output : 30
#12 + 22 + 32 + 42
#= 1 + 4 + 9 + 16
#= 30

#Input : N = 5
#Output : 55

def  sum_of_squares(num):
    cnt=1
    sum=0
    while(cnt<=num):
        square=pow(cnt,2)
        sum+=square
        cnt+=1
    return sum

Number=int(input("Enter the Number: "))
print(sum_of_squares(Number))
