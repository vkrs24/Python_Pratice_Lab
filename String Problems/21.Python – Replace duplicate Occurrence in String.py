# 22Sept2024
# 21.Python – Replace duplicate Occurrence in String

# repl_dict = {'Gfg' : 'It', 'Classes' : 'They' } 

# The original string is : Gfg is best . Gfg also has Classes now. 
# Classes help understand better . 

# The string after replacing : Gfg is best . 
# It also has Classes now. They help understand better .

def replace(s,rs):
    dict={}
    RS=rs.split()
    S=s.split()
    for i in RS:
        k,v=i.split(':')
        dict[k]=v
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            if(S[i]==S[j]) and S[i] in dict:
                key=S[i]
                S[j]=dict[key]
    print(" ".join(S))


replace("Gfg is best . Gfg also has Classes now. Classes help understand better . ","Gfg:It Classes:They")