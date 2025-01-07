#6Lovember2024
#5.Merging or Concatenating two Dictionaries in Python

# Input: d1 = {‘a’: 10, ‘b’: 8},      
#            d2 = {‘d’: 6, ‘c’: 4}
# Output: {‘a’: 10, ‘b’: 8, ‘d’: 6, ‘c’: 4}

def merge(d1,d2):
    d3={}
    d3.update(d1)
    d3.update(d2)
    print(d3)

d1 = {'a': 10, 'b': 8}     
d2 = {'d': 6, 'c': 4}

merge(d1,d2)