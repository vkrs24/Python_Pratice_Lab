# 17Sept2024
# 6.Python – Words Frequency in String Shorthands

# Input : test_str = 'Gfg is best' 
# Output : {'Gfg': 1, 'is': 1, 'best': 1} 

# Input : test_str = 'Gfg Gfg Gfg' 
# Output : {'Gfg': 3}

def word_frequency(s):
    S=s.split()
    dic={}
    for i in S:
        if i not in dic:
            dic[i]=S.count(i)
    print(dic)

word_frequency('Gfg is best')
word_frequency('Gfg Gfg Gfg')