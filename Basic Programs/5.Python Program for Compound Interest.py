#26June2025
#Basic Programs
#5.Python Program for Compound Interest
#Input:
#Enter the principal amount: 3000
#Enter rate of interest: 5
#Enter time in years: 3
#Output:
#Compound interest is 472.875
#Hint:
#A = P(1 + R/100) t 
#Compound Interest = A – P 
#Where, 
#A is amount 
#P is the principal amount 
#R is the rate and 
#T is the time span

def Compound_Interest(principal,rate,time):
        amount = principal*pow((1 + (rate/100)),time)
        return format(amount-principal,'.3f')

Amount=int(input('Enter the principal amount: '))
Intrest=int(input('Enter rate of interest: '))
Years=int(input('Enter time in years: '))
print(f'Compound interest is {Compound_Interest(Amount, Intrest, Years)}')
