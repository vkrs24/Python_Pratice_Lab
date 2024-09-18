# 16Sept2024
# 2.Python program to check whether the string is Symmetrical or Palindrome

# Input: khokho
# Output: 
# The entered string is symmetrical
# The entered string is not palindrome

# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome

def check_palindrome_and_symmetric(s):
    rev_s=""
    S_bool=True
    P_bool=True
    indx=0
    for i in range(len(s)-1,-1,-1):
        rev_s+=s[i]
    for i in range(len(s)):
        if(s[i]!=rev_s[i]):
            P_bool=False
            break
    for i in range((len(s)//2),len(s)):
        if(s[indx]!=s[i]):
            S_bool=False
            break
        indx+=1
    if(S_bool):
        print("It is Symmetrical")
    else:
        print("It is not Symmetrical")
    if(P_bool):
        print("It is Palindrome")
    else:
        print("It is not Palindrome")

check_palindrome_and_symmetric("khokho")
check_palindrome_and_symmetric("amaama")

    