def nth_fibonacci(pos):
    if(pos==1):
        return 0
    if(pos==2):
        return 1
    else:
        return nth_fibonacci(pos-1)+nth_fibonacci(pos-2)

print(nth_fibonacci(9))
