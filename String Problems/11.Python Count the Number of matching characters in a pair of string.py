# 18Sept2024
# 11.Python | Count the Number of matching characters in a pair of string

# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4 
# (i.e. matching characters :- a, d, e, f)

# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb2211@55k'
# Output : 5 
# (i.e. matching characters :- b, 1, 2, @, k)

def match_character(s1,s2):
    cnt=0
    for i in s1:
        if(i in s2):
            cnt+=1
    print(cnt)

match_character('abcdef','defghia')
match_character('aabcddekll12@','bb2211@55k')