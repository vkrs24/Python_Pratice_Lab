# 14Sept2024
# 23.Python | Cloning or Copying a list

# Original List: [4, 8, 2, 10, 15, 18]
 
# After Cloning: [4, 8, 2, 10, 15, 18] 

def clone(arr):
    lst=[]
    for i in arr:
        lst.append(i)
    print(lst)

    lst2=[]
    lst2.extend(lst)
    print(lst2)
    

clone([4, 8, 2, 10, 15, 18])