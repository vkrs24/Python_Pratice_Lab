# 25Sept2024
# 28.Python – Replace all occurrences of a substring in a string

# Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
# Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

# Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
# Output : test_str = “geeksabcdgeeks”

def replace_occurrence(ts,s,rs):
    new_string=""
    for i in range(len(ts)):
        if(ts[i:i+len(s)]==s[0:]):
            new_string+=rs
        else:
            if(ts[i] not in s):
                new_string+=ts[i]
        
    print(new_string)
        
replace_occurrence("geeksforgeeks","geeks","abcd")
replace_occurrence("geeksforgeeks","for","abcd")