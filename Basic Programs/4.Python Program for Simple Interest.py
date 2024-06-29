#26June2025
#Basic Programs
#4.Python Program for Simple Interest
#Input:
#P = 10000
#R = 5
#T = 5
#Output:
#2500.0
#We need to find simple interest on Rs. 10,000 at the rate of 5%
#for 5 units of time.
#Hint:Simple interest formula is given by: Simple Interest = (P x T x R)/100
#Where, P is the principal amount T is the time and R is the rate.

def simple_intrest(p,r,t):
    simple_intrest_result=(p*r*t)/100;
    return float(simple_intrest_result)

P=int(input('P :'))
R=int(input('R :'))
T=int(input('T :'))
print(simple_intrest(P,R,T))
