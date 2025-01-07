#8Lovember2024
#8.Python | Check order of character in string using OrderedDict( )

# Input: 
# string = "engineers rock"
# pattern = "er";
# Output: true
# Explanation: 
# All 'e' in the input string are before all 'r'.

# Input: 
# string = "engineers rock"
# pattern = "gsr";
# Output: false
# Explanation:
# There are one 'r' before 's' in the input string.

def check_order(s,p):
    idx=0
    cnt=0
    for i in range(len(p)):
        print(p[i])
        for j in s[idx:]:
            if(p[i]==j)and(p[i+1] not in s[:idx+1]):
                cnt+=1
                idx+=1z
                print(j)
                break
        idx+=1
    print(cnt)



string = "engineers rock"
pattern = "gsr"
check_order(string,pattern)
string = "engineers rock"
pattern = "er"
check_order(string,pattern)