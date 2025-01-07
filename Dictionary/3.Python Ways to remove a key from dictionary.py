#5Lovember2024
#3.Python | Ways to remove a key from dictionary

# Output :
# The dictionary before performing remove is :  {'Arushi': 22, 'Mani': 21,
#  'Haritha': 21}
# The dictionary after remove is :  {'Arushi': 22, 'Haritha': 21}

def remove_dict(dic):
    print(dic)
    del dic['Mani']
    print(dic)

dic={'Arushi': 22, 'Mani': 21, 'Haritha': 21}
remove_dict(dic)