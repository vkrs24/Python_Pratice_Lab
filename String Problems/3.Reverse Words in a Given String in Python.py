# 17Sept2024
# 3.Reverse Words in a Given String in Python

# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks
  
# Input : str = "my name is laxmi"
# output : str= laxmi is name my 

def reverse_word(s):
    S=s.split(" ")
    S.reverse()
    for i in S:
        if(i==" "):
            continue
        print(i,end=" ")
    
    print()
reverse_word(" geeks quiz practice code")
reverse_word("my name is laxmi")
