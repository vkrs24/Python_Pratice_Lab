# 25Sept2024
# 27.Python – Find all duplicate characters in string

# Input : hello
# Output : l

# Input : geeksforgeeeks
# Output : e g k s

def print_duplicate(s):
    S=""
    for i in s:
        if i not in S:
            if(s.count(i)>1):
                S+=i
    print(S)

def dict_duplicate(s):
    dict={}
    S=""
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
            if(dict[i]==2):
                S+=i
    print(S)
    


print_duplicate("hello")
print_duplicate("geeksforgeeeks")

dict_duplicate("hello")
dict_duplicate("geeksforgeeeks")
