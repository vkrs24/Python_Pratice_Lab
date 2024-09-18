# 18Sept2024
# 12.Remove All Duplicates from a Given String in Python

# Input : geeksforgeeks 
# Output : geksfor

def remove_duplicate(s):
    S=""
    for i in range(len(s)):
        f=0
        for j in range(0,i):
            if i==j:
                continue
            elif s[i]==s[j]:
                f=1
                break
        if f==0:
            S+=s[i]
    print(S)

def rmv_duplic(s):
    dict={}
    S=""
    for i in range(len(s)):
        if(s[i] not in dict):
            dict[s[i]]=1
            S+=s[i]
        else:
            continue
    print(S)
    
def rmv_dpl(s):
    t=""
    for i in s:
        if i in t:
            continue
        else:
            t+=i
    print(t)

    
remove_duplicate('geeksforgeeks')
rmv_duplic('geeksforgeeks')
rmv_dpl('geeksforgeeks')