# 14Sept2024
# 19.Python program to print all positive numbers in a range

# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5 

# Input: start = -3, end = 4
# Output: 0, 1, 2, 3, 4

def all_positive(start,end):
    lst=[]
    if(start<0):
        start=0
    for i in range(start,end+1):
        lst.append(str(i))
    print(','.join(lst))
    print()

all_positive(-4,5)
all_positive(-3,4)