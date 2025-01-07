def amstrong(num):
    num_str=len(str(num))
    sum=0
    for i in str(num):
        sum+=(int(i)**num_str)
    if(sum==num):
        print("Amstrong")
    else:
        print("Not An Amstrong")

amstrong(153)
amstrong(120)
    
