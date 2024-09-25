# 22Sept2024
# 18.Python program to split and join a string

# Split the string into list of strings

# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']


# Join the list of strings into a string based on delimiter ('-')

# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks

def split_and_join(s):
    if(type(s)==str):
        S=s.split()
    else:
        S=s
    print(S)
    print('-'.join(S))

split_and_join("Geeks for Geeks")
split_and_join(['Geeks', 'for', 'Geeks'])