# 16Sept2024
# 7.Python | Get Kth Column of Matrix

# K:2 

# The original list is : [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

# The Kth column of matrix is : [6, 10, 5]

def get_kth(k,matrix):
    lst=[]
    for i in range(len(matrix)):
        lst.append(matrix[i][k])
    print(lst)

matrix=[[4, 5, 6], [8, 1, 10], [7, 12, 5]]
get_kth(2,matrix)