# 14Sept2024
# 24.Python | Count occurrences of an element in a list

# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10

# Output: 3 

# Explanation: 10 appears three times in given list.

# Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16

# Output: 0

# Explanation: 16 appears zero times in given list.

def count(arr,x):
    count=0
    for i in arr:
        if(i==x):
            count+=1
    print(count)

count([15, 6, 7, 10, 12, 20, 10, 28, 10],10)
count([8, 6, 8, 10, 8, 20, 10, 8, 8],16)
