# 25Sept2024
# 24.Python | Check for URL in a String

# Input : string = 'My Profile: 
# https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
# in the portal of https://www.geeksforgeeks.org/'

# Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy
#                  %20Lenka/articles',
# 'https://www.geeksforgeeks.org/']

# Input : string = 'I am a blogger at https://geeksforgeeks.org'
# Output : URL :  ['https://geeksforgeeks.org']

def check_url(s):
    S=s.split()
    for i in S:
        if i[0:5] == "https":
            print(i)
        
    
check_url("My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/")
check_url("I am a blogger at https://geeksforgeeks.org")