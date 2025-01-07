def factorial(num):
    while(num>0):
        fact=num
        return fact*factorial(num-1)
    if(num==0):
        return 1
    

print(factorial(3))
