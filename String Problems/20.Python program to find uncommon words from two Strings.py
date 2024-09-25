# 22Sept2024
# 20.Python program to find uncommon words from two Strings

# Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
# Output : [‘Learning’, ‘from’]

# Input : A = “apple banana mango” , B = “banana fruits mango”
# Output : [‘apple’, ‘fruits’]

def uncommon_words(A,B):
    A=A.split()
    B=B.split()
    A.extend(B)
    N=[]
    for i in A:
        if(A.count(i)>1):
            continue
        else:
            N.append(i)
    print(N)


uncommon_words("Geeks for Geeks","Learning from Geeks for Geeks")
uncommon_words("apple banana mango","banana fruits mango")