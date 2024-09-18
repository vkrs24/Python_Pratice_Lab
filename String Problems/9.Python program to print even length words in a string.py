# 18Sept2024
# 9.Python program to print even length words in a string

# Input: s = "This is a python language"
# Output: This is python language

# Input: s = "i am laxmi"
# Output: am

def even_length(s):
    S=s.split()
    for i in S:
        if(len(i)%2==0):
            print(i,end=" ")
    print()
    

even_length("This is a python language")
even_length("i am laxmi")