def prime(num):
    for i in range(2,num+1):
        flag=0;
        for j in range(2,i//2+1):
            if(i%j==0):
                flag=1
        if(flag==0):
            print(i)

prime(19)

