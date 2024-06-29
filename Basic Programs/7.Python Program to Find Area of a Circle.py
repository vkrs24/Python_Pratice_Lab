#27June2025
#Basic Programs
#7.Python Program to Find Area of a Circle
#The area of a circle can simply be evaluated using the following formula.
#Area = pi * r2
#where r is radius of circle
#Input:
#5
#Output:
#Area is 78.550000

def area_of_circle(radius):
    area=3.142*pow(radius,2)
    return format(area,'.6f')
Radius=int(input("Enter the radius: "))
print(f'Area is {area_of_circle(Radius)}')
