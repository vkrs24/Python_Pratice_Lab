#8Lovember2024
#7.Python – Insertion at the beginning in OrderedDict

#Input: 
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)

# Output:  
# {'c':3, 'a':1, 'b':2}

def insert_at_beginning(o_d,i_d):
    ins_dic={}
    for i in range(0,len(i_d),2):
        ins_dic[i_d[i]]=i_d[i+1]
    for k,v in o_d.items():
        if(k not in ins_dic):
            ins_dic[k]=v
    print(ins_dic)

insert_at_beginning({'a':1, 'b':2},('c', 3))