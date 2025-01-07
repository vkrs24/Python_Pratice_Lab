<<<<<<< HEAD
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
=======
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
>>>>>>> c646c3f14aced55b9d98f51205aad3f2c12562f2
even_length("i am laxmi")