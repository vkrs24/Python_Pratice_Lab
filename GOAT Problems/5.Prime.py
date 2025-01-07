def prime(num):
    if num>1:
        flag=0
        for i in range(2,num//2+1):
            if(num%i==0):
                flag=1
                break
        if(flag!=1):
            print("Prime")
        else:
            print("Not Prime")


prime(2)
prime(3)
prime(4)
prime(5)
