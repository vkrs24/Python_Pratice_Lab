# 16thSept2024
# 5.Python | Matrix Product

# The original list : [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# The total element product in lists is : 1622880

def Matrix_product(m):
    prod=1
    for i in range(len(m)):
        for j in range(len(m[i])):
            prod*=m[i][j]
    print(prod)

Matrix_product([[1, 4, 5], [7, 3], [4], [46, 7, 3]])