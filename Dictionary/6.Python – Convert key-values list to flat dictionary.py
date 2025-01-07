#6Lovember2024
#6.Python – Convert key-values list to flat dictionary

# The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: 
# [1, 2, 3]} 

# Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}

def convert(dict):
    c_dic={}
    name=dict['name']
    month=dict['month']
    for i in range(len(name)):
        c_dic[month[i]]=name[i]
    print(c_dic)
    


dict={'name': ['Jan', 'Feb', 'Marc'], 'month': [1, 2, 3]} 
convert(dict)

