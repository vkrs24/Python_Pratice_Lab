#26June2025
#Basic Programs
#6.Python Program to Check Armstrong Number
#Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

#abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
#Example:

#Input : 153
#Output : Yes
#153 is an Armstrong number.
#1*1*1 + 5*5*5 + 3*3*3 = 153

#Input : 120
#Output : No
#120 is not a Armstrong number.
#1*1*1 + 2*2*2 + 0*0*0 = 9

def amstrong_check(counts,num):
    amst_result=0
    while(num!=0):
        reminder=num%10
        amst_result+=pow(reminder,counts)
        num=num//10
    return amst_result

def digit(number):
    counts=0
    num=number
    quotient=number//10
    while(quotient!=0):
        quotient=number//10
        counts+=1
        number=quotient
    return amstrong_check(counts,num)

Number=int(input('Enter the Number: '))
result=digit(Number)
amstrong_result_1=''
amstrong_result_2=''
if(Number==result):
    amstrong_result_1='Yes'
    amstrong_result_2='an'
else:
    amstrong_result_1='No'
    amstrong_result_2='not a'
    
print(f'{amstrong_result_1}')
print(f'{Number} is {amstrong_result_2} Armstrong Number')
