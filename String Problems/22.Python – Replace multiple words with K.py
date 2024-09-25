# 22Sept2024
# 22.Python – Replace multiple words with K


# word_list = ["best", 'CS', 'for'] 

# repl_wrd = 'gfg'

# The original string is : Geeksforgeeks is best for geeks and CS

# String after multiple replace : Geeksforgeeks is gfg gfg geeks and gfg

def replace_with_k(s,wtr,rw):
    S=s.split()
    WTR=wtr.split()
    for i in WTR:
        for index,j in enumerate(S):
            if(i==j):
                S[index]=rw
    print(" ".join(S))

replace_with_k("Geeksforgeeks is best for geeks and CS","best CS for","gfg")