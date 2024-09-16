# 15Sept2024
# 4.Transpose a matrix in Single line in Python

# Input: [[1,2],[3,4],[5,6]]
# Output: [[1,3,5],[2,4,6]]
# Explanation: Suppose we are given a matrix
#                        [[1, 2],
#                         [3, 4],
#                         [5, 6]]
# Then the transpose of the given matrix will be, 
#                        [[1, 3, 5],
#                         [2, 4, 6]]

# Input: [(1, 2, 3), (4, 5, 6),(7, 8, 9), (10, 11, 12)]

# Output:
# (1, 4, 7, 10)
# (2, 5, 8, 11)
# (3, 6, 9, 12)  

def transpose_matrix(m1):
    arr=[[0 for j in range(len(m1))] for i in range(len(m1[0]))]
    for i in range(len(m1[0])):
        for j in range(len(m1)):
            arr[i][j]=m1[j][i]
    print(arr)
    print()

A=[[1,2],[3,4],[5,6]]
B=[(1, 2, 3), (4, 5, 6),(7, 8, 9), (10, 11, 12)]
transpose_matrix(A)
transpose_matrix(B)