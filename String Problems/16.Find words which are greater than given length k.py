<<<<<<< HEAD
# 22Sept2024
# 16.Find words which are greater than given length k

# Input : str = "hello geeks for geeks 
#           is computer science portal" 
#         k = 4
# Output : hello geeks geeks computer 
#          science portal
# Explanation : The output is list of all 
# words that are of length more than k.

# Input : str = "string is fun in python"
#         k = 3
# Output : string python 

def g_length(s,k):
    S=s.split()
    for i in S:
        if(len(i)>k):
            print(i,end=" ")
    print()

g_length("hello geeks for geeks is computer science portal",4)
=======
# 22Sept2024
# 16.Find words which are greater than given length k

# Input : str = "hello geeks for geeks 
#           is computer science portal" 
#         k = 4
# Output : hello geeks geeks computer 
#          science portal
# Explanation : The output is list of all 
# words that are of length more than k.

# Input : str = "string is fun in python"
#         k = 3
# Output : string python 

def g_length(s,k):
    S=s.split()
    for i in S:
        if(len(i)>k):
            print(i,end=" ")
    print()

g_length("hello geeks for geeks is computer science portal",4)
>>>>>>> c646c3f14aced55b9d98f51205aad3f2c12562f2
g_length("string is fun in python",3)