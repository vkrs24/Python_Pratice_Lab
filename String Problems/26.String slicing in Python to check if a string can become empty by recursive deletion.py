# 25Sept2024
# 26.String slicing in Python to check if a string can become empty 
# by recursive deletion

# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes
# Explanation : In the string GEEGEEKSKS, we can first 
#               delete the substring GEEKS from position 4.
#               The new string now becomes GEEKS. We can 
#               again delete sub-string GEEKS from position 1. 
#               Now the string becomes empty.


# Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
# Output : No
# Explanation : In the string it is not possible to make the
#               string empty in any possible manner.


def empty_string(s,ss):
    if(len(s)==0):
        return 'Yes'
    
    for i in range(len(s)-len(ss)+1):
        if(s[i:i+len(ss)]==ss[0:]):
            s=s[:i]+s[i+len(ss):]
            return empty_string(s,ss)
    return "No"

print(empty_string("GEEGEEKSKS","GEEKS"))
print(empty_string("GEEGEEKSSGEK","GEEKS"))
    