# 14Sept2024
# 1.Python Program to Add Two Matrices

# Input :
#  X= [[1,2,3],
#     [4 ,5,6],
#     [7 ,8,9]]
 
# Y = [[9,8,7],
#     [6,5,4],
#     [3,2,1]]
 
# Output :
#  result= [[10,10,10],
#          [10,10,10],
#          [10,10,10]]

def sum_of_matrix(m1,m2):
    arr=[]
    for i in range(len(m1)):
        value=[m1[i][j]+m2[i][j] for j in range(len(m2[0]))]
        arr.append(value)
    print(arr)

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

sum_of_matrix(X,Y)

        