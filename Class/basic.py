class Myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"
    
person_1=Myclass("Vasanthakumar",20)
print(person_1)
        