<<<<<<< HEAD
# 18sept2024
# 15.Program to check if a string contains any special character

# Input: Geeks$For$Geeks
# Output: String is not accepted.

# Input: Geeks For Geeks
# Output: String is accepted

def rmv_spl_char(s):
    for i in s:
        if(i.isalpha() or i==" "):
            f=1
        else:
            f=0
            print("String is not accepted")
            break
    if(f):
        print("string is accepted")

rmv_spl_char("Geeks$For$Geeks")
=======
# 18sept2024
# 15.Program to check if a string contains any special character

# Input: Geeks$For$Geeks
# Output: String is not accepted.

# Input: Geeks For Geeks
# Output: String is accepted

def rmv_spl_char(s):
    for i in s:
        if(i.isalpha() or i==" "):
            f=1
        else:
            f=0
            print("String is not accepted")
            break
    if(f):
        print("string is accepted")

rmv_spl_char("Geeks$For$Geeks")
>>>>>>> c646c3f14aced55b9d98f51205aad3f2c12562f2
rmv_spl_char("Geeks For Geeks")