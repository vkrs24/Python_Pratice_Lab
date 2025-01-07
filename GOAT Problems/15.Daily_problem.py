string=input()
lst=[]
l=[val for val in string.split()]
for i in l:
    w_cnt=string.count(i)
    if i not in lst:
        if(w_cnt>1):
            lst.append(i)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(len(lst[i])>=len(lst[j])):
            lst[i],lst[j]=lst[j],lst[i]
lst.reverse()
for i in lst:
    print(i,end=" ")
    
