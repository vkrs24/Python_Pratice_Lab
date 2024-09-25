# 22Sept2024
# 17.Python program for removing i-th character from a string

# g e e k s
# 0 1 2 3 4
# Examples :

# Input : Geek
#         i = 1
# Output : Gek

# Input : Peter 
#         i = 4
# Output : Pete

def remove_index_element(s,i):
    S=[val for val in s]
    for j in range(len(S)):
        if(j==i):
            continue
        else:
            print(S[j],end="")
    print()
remove_index_element("Geek",1)
remove_index_element("Peter",4)
