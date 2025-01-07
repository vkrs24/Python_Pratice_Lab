def fibonacci(num):
    f=0
    s=1
    for i in range(num):
        print(f)
        r=f+s
        s=f
        f=r

fibonacci(9)
