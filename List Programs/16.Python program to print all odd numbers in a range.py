#14Sept2024
# 16.Python program to print all odd numbers in a range

# Input: start = 4, end = 15
# Output: 5, 7, 9, 11, 13, 15

# Input: start = 3, end = 11
# Output: 3, 5, 7, 9, 11

def odd(s,e):
    for i in range(s,e+1):
        if(i%2!=0):
            print(i,end=" ")
    
start,End=map(int,input().split())
odd(start,End)