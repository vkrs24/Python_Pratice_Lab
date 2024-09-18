# 18Sept2024
# 8.Find length of a string in python

# Input : 'abc'
# Output : 3

# Input : 'hello world !'
# Output : 13

# Input : ' h e l   l  o '
# Output :14

def length(s):
    cnt=0
    for i in s:
        cnt+=1
    print(cnt)

length('abc')
length('hello world !')
length(' h e l   l  o ')