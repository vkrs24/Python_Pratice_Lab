# 14Sept2024
# 20.Python program to print all negative numbers in a range

# Input: a = -4, b = 5
# Output: -4, -3, -2, -1

# Input: a = -3, b= 4
# Output: -3, -2, -1

def all_negative(start,end):
    lst=[]
    if(end>-1):
        end=0
    for i in range(start,end):
        lst.append(str(i))
    print(', '.join(lst))
    print()

all_negative(-4,5)
all_negative(-3,4)