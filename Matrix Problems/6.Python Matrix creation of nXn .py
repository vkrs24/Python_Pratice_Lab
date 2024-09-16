# 16Sept2024
# 6.Python | Matrix creation of n*n

# The dimension : 4

# The created matrix of N * N: 
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def matrix_creation(n):
    matrix=[]
    lst=[]
    val=1
    for i in range(n):
        for j in range(n):
            lst.append(val)
            val+=1
        matrix.append(lst)
        lst=[]
    print(matrix)

matrix_creation(4)
matrix_creation(5)