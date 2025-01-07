# 14Sept2024
# 26.Sort the values of first list using second list in Python

# Input : list1 = [“a”, “b”, “c”, “d”, “e”, “f”, “g”, “h”, “i”]
#            list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# Output : [‘a’, ‘d’, ‘h’, ‘b’, ‘c’, ‘e’, ‘i’, ‘f’, ‘g’]

# Input : list1 = [“g”, “e”, “e”, “k”, “s”, “f”, “o”, “r”, “g”, “e”, “e”, “k”, “s”]
#             list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
# Output : [‘g’, ‘k’, ‘r’, ‘e’, ‘e’, ‘g’, ‘s’, ‘f’, ‘o’]

def sort_l1_using_l2(l1,l2):
    lst=[]
    tpl=set(l2)
    for i in tpl:
        for j in range(len(l2)):
            if(l2[j]==i):
                lst.append(l1[j])
    print(lst)

sort_l1_using_l2(['a','b','c','d','e','f','g','h','i'], [ 0,   1,   1,    0,   1,   2,   2,   0,   1])
sort_l1_using_l2(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'], [ 0,   1,   1,    0,   1,   2,   2,   0,   1])
