<<<<<<< HEAD
# 17Sept2024
# 4.How to Remove Letters From a String in Python

# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.

def remove_numeric(s):
    for i in s:
        if(i.isalpha()):
            print(i,end="")
        
=======
# 17Sept2024
# 4.How to Remove Letters From a String in Python

# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.

def remove_numeric(s):
    for i in s:
        if(i.isalpha()):
            print(i,end="")
        
>>>>>>> c646c3f14aced55b9d98f51205aad3f2c12562f2
remove_numeric("Geeks123For123Geeks")