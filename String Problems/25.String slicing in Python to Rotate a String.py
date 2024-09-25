# 25Sept2024
# 25.String slicing in Python to Rotate a String

# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe" 
#          Right Rotation : "ksGeeksforGee"  


# Input : s = "qwertyu" 
#         d = 2
# Output : Left rotation : "ertyuqw"
#          Right rotation : "yuqwert"

def rotate(s,d):
    left=s[d:]+s[:d]
    right=s[len(s)-d:]+s[:len(s)-d]
    print(left)
    print(right)

rotate("qwertyu",2)
rotate("GeeksforGeeks",2)