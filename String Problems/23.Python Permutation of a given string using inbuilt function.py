<<<<<<< HEAD
# 22Sept2024

# 23.Python | Permutation of a given string using inbuilt function

# Input :  str = 'ABC'
# Output : ABC 
#          ACB 
#          BAC 
#          BCA 
#          CAB 
#          CBA

# Input :  str = 'GEEK'
#Output : GEEK
#         GEKE
#         GKEE
#         EGEK
#         EGKE
#         EEGK
#         EEKG
#         EKGE
#         EKEG
#         KGEE
#         KEGE
#         KEEG

from itertools import permutations as per
st="ABC"
permu=per(st)
for i in permu:
=======
# 22Sept2024

# 23.Python | Permutation of a given string using inbuilt function

# Input :  str = 'ABC'
# Output : ABC 
#          ACB 
#          BAC 
#          BCA 
#          CAB 
#          CBA

# Input :  str = 'GEEK'
#Output : GEEK
#         GEKE
#         GKEE
#         EGEK
#         EGKE
#         EEGK
#         EEKG
#         EKGE
#         EKEG
#         KGEE
#         KEGE
#         KEEG

from itertools import permutations as per
st="ABC"
permu=per(st)
for i in permu:
>>>>>>> c646c3f14aced55b9d98f51205aad3f2c12562f2
    print(i)