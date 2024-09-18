# 16Sept2024
# 1.Python Program to Check if a String is Palindrome or Not

# Input : malayalam
# Output : Yes
# Input : geeks
# Output : No

def check_palindrome(s):
    rev_s=""
    bool=True
    for i in range(len(s)-1,-1,-1):
        rev_s+=s[i]
    for i in range(len(s)):
        if(s[i]!=rev_s[i]):
            bool=False
            break
    if(bool):
        print("Yes")
    else:
        print("No")

check_palindrome("malayalam")
check_palindrome("greeks")