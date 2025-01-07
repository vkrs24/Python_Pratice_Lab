#29June2025
#Basic Programs
#15.Python Program for cube sum of first n natural numbers
#Write a Python program to print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till the n-th term. 

#Examples:

#Input: n = 5
#Output: 225
#Explanation: 13 + 23 + 33 + 43 + 53 = 225

#Input: n = 7
#Output: 784
#Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784

def  sum_of_cubes(num):
    cnt=1
    sum=0
    while(cnt<=num):
        square=pow(cnt,3)
        sum+=square
        cnt+=1
    return sum

Number=int(input("Enter the Number: "))
print(sum_of_cubes(Number))
