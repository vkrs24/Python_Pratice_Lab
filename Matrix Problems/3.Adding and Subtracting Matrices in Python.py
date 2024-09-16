# 14Sept2024
# 3.Adding and Subtracting Matrices in Python

# Suppose we have two matrices A and B.
# A = [[1,2],[3,4]]
# B = [[4,5],[6,7]]

# then we get
# A+B = [[5,7],[9,11]]
# A-B = [[-3,-3],[-3,-3]]

def matrix_addition_and_subraction(m1,m2):
    arr1=[[0 for j in range(len(m2[i]))] for i in range(len(m1))]
    arr2=[[0 for j in range(len(m2[i]))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2)):
            arr1[i][j]=m1[i][j]+m2[i][j]
            arr2[i][j]=m1[i][j]-m2[i][j]
    print(arr1)
    print(arr2)

A = [[1,2],[3,4]]
B = [[4,5],[6,7]]
matrix_addition_and_subraction(A,B)
