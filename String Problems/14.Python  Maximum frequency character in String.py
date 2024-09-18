# 18Sept2024
# 14.Python | Maximum frequency character in String
#Input:  The original string is : GeeksforGeeks

#Output: The minimum of all characters in GeeksforGeeks is : f

def max_frequency(s):
    t=[]
    idx=[]
    for i in s:
        if(i in t):
            pass
        else:
            t.append(i)
            idx.append(s.count(i))
    print(t[idx.index(max(idx))])
    

def maximum_frequency(s):
    dict={}
    for i in s:
        if(i not in dict):
            dict[i]=s.count(i)
    maxi=max(dict.values())
    for key,value in dict.items():
        if(maxi==value):
            print(key)
            break




max_frequency("GeeksforGeeks")
maximum_frequency("GeeksforGeeks")