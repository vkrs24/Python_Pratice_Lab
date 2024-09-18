# 18Sept2024
# 10.Python Program to Accept the Strings Which Contains all Vowels

# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present

# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present

def vowels_in_string(s):
    vowels="aeiou"
    result="Accepted"
    s=s.lower()
    for i in vowels:
        if(i not in s):
            result="Not Accepted"
            break
    print(result)

vowels_in_string('geeksforgeeks')
vowels_in_string('ABeeIghiObhkUul')
            