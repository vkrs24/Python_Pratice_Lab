# 14Sept2024
# 2.Python program to multiply two matrices

# Input : X = [[1, 7, 3],
#              [3, 5, 6],
#              [6, 8, 9]]
#        Y = [[1, 1, 1, 2],
#            [6, 7, 3, 0],
#            [4, 5, 9, 1]]
 
# Output : [55, 65, 49, 5]
#          [57, 68, 72, 12]
#          [90, 107, 111, 21]

# A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
# B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

# [114, 160, 60, 27]
# [74, 97, 73, 14]
# [119, 157, 112, 23]

def matrix_multiplication(m1,m2):
    arr=[]
    val=[]
    col=0
    value=0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for l in range(len(m1)):
                value+=(m1[i][col]*m2[l][j])
                col+=1
            col=0
            val.append(value)
            value=0
        arr.append(val)
        val=[]
        print(arr[i])
    print()
    

X = [[1, 7, 3],
    [3, 5, 6],
    [6, 8, 9]]

Y = [[1, 1, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

matrix_multiplication(X,Y)
matrix_multiplication(A,B)