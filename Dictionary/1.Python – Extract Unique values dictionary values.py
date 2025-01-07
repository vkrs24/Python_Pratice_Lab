#5Lovember2024
#1.Python – Extract Unique values dictionary values

#input: 
# The original dictionary is : {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5],
#       'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

#output: 
# The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]

def extract_unique(dic):
    unique=[]
    for k,v in dic.items():
        for i in v:
            if i not in unique:
                unique.append(i)
    unique.sort()
    print(unique)

dic={'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5],'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
extract_unique(dic)