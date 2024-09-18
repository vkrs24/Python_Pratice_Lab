# 17Sept2024
# 4.How to Remove Letters From a String in Python

# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.

def remove_numeric(s):
    for i in s:
        if(i.isalpha()):
            print(i,end="")
        
remove_numeric("Geeks123For123Geeks")