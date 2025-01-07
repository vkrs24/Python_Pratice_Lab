#7thJuly2024
#15.Python program to print all even numbers in a range

#Input: start = 4, end = 15
#Output: 4, 6, 8, 10, 12, 14

#Input: start = 8, end = 11
#Output: 8, 10

def print_all_even_numbers(start,end):
    for i in range(start,end+1):
        if(i%2==0):
            print(f"{i}")

print_all_even_numbers(4,15)
print("\n")
print_all_even_numbers(8,11)
