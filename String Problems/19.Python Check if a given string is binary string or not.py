# 22Sept2024
# 19.Python | Check if a given string is binary string or not

# Input: str = "01010101010"
# Output: Yes

# Input: str = "geeks101"
# Output: No

def binary_string(s):
    cnt=0
    for i in s:
        if(i.isdigit()):
            cnt+=1
        else:
            print("No")
            break
    if(cnt==len(s)):
        print("Yes")

binary_string("01010101010")
binary_string("geeks101")