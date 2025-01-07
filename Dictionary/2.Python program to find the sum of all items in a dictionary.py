#5Lovember2024
#2.Python program to find the sum of all items in a dictionary

# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

# Input : {‘x’: 25, ‘y’:18, ‘z’:45}
# Output : 88

def sum_of_dict_items(dic):
    sum=0
    for i in dic:
        sum+=dic[i]
    print(sum)

dic1={'a': 100, 'b': 200, 'c': 300}
sum_of_dict_items(dic1)

dic2={'x': 25, 'y':18, 'z':45}
sum_of_dict_items(dic2)