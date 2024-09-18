# 17Sept2024
# 5.Check if String Contains Substring in Python

# Input: Substring = "geeks" 
#             String="geeks for geeks"
# Output: yes
# Input: Substring = "geek"
#            String="geeks for geeks"
# Output: yes
# Explanation: In this, we are checking if the substring is present in a 
# given string or not.

def find_substring(s,ss):
    for i in range(len(s)):
        cnt=0
        indx=0
        for j in range(len(ss)):
            if(s[indx]==ss[j]):
                cnt+=1
            indx+=1
        if(cnt==len(ss)):
            print("Yes")
            break
        else:
            print("No")
            break
    
find_substring("geeks for geeks","geek")
find_substring("geeks for geeks","greek")