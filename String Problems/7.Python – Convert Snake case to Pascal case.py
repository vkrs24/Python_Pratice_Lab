# 18Sept2024
# 7.Python – Convert Snake case to Pascal case

# Input : geeks_for_geeks Output : GeeksforGeeks 

# Input : left_index Output : leftIndex

def snake_to_pascal(s):
    S=""
    for i in s:
        if(i!="_"):
            S+=i

    print(S)

snake_to_pascal('geeks_for_geeks')
snake_to_pascal('left_index')

