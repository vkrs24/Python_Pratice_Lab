# 16Sept2024
# 8.Python – Vertical Concatenation in Matrix

# Input : [[“Gfg”, “good”], [“is”, “for”]] 

# Output : [‘Gfgis’, ‘goodfor’] 

# Explanation : Column wise concatenated Strings, 
# “Gfg” concatenated with “is”, and so on. 

# Input : [[“Gfg”, “good”, “geeks”], [“is”, “for”, “best”]] 

# Output : [‘Gfgis’, ‘goodfor’, “geeksbest”] 

# Explanation : Column wise concatenated Strings, 
# “Gfg” concatenated with “is”, and so on.

def concatenation_of_matrix(matrix):
    lst=[]
    x=""
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            x+=matrix[j][i]
        lst.append(x)
        x=""
    print(lst)

matrix1=[["Gfg", "good"], ["is", "for"]] 
matrix2=[["Gfg", "good", "geeks"], ["is", "for", "best"]]
concatenation_of_matrix(matrix1)
concatenation_of_matrix(matrix2)