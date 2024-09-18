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
rmv_spl_char("Geeks For Geeks")