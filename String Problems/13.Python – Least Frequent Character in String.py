<<<<<<< HEAD
# 18Sept2024
# 13.Python – Least Frequent Character in String

#Input:  The original string is : GeeksforGeeks

#Output: The minimum of all characters in GeeksforGeeks is : f

def min_frequency(s):
    t=[]
    idx=[]
    for i in s:
        if(i in t):
            pass
        else:
            t.append(i)
            idx.append(s.count(i))
    print(t[idx.index(min(idx))])
    

def minimum_frequency(s):
    dict={}
    for i in s:
        if(i not in dict):
            dict[i]=s.count(i)
    mini=min(dict.values())
    for key,value in dict.items():
        if(mini==value):
            print(key)
            break




min_frequency("GeeksforGeeks")
=======
# 18Sept2024
# 13.Python – Least Frequent Character in String

#Input:  The original string is : GeeksforGeeks

#Output: The minimum of all characters in GeeksforGeeks is : f

def min_frequency(s):
    t=[]
    idx=[]
    for i in s:
        if(i in t):
            pass
        else:
            t.append(i)
            idx.append(s.count(i))
    print(t[idx.index(min(idx))])
    

def minimum_frequency(s):
    dict={}
    for i in s:
        if(i not in dict):
            dict[i]=s.count(i)
    mini=min(dict.values())
    for key,value in dict.items():
        if(mini==value):
            print(key)
            break




min_frequency("GeeksforGeeks")
>>>>>>> c646c3f14aced55b9d98f51205aad3f2c12562f2
minimum_frequency("GeeksforGeeks")