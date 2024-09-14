# 14Sept2024
# 25.Python | Remove empty tuples from a list

# Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), 
# (‘krishna’, ‘akbar’, ’45’), (”,”),()]

# Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’,
#  ’45’), (”, ”)]

# Input : tuples = [(”,”,’8′), (), (‘0′, ’00’, ‘000’), (‘birbal’, ”,
#  ’45’), (”), (),  (”,”),()]

# Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]

def remove_empty(tpl):
    tpl2=[]
    for i in tpl:
        if(i!=()):
            tpl2.append(i)
    print(tpl2)

remove_empty([(),('ram', '15', '8'), ('laxman', 'sita'),(), ('krishna', 'akbar',
'45'),(), ('', '')])

remove_empty([('','','8'), (), ('0', '00', '000'), ('birbal','',
'45'), (''), (),  ('',''),()])