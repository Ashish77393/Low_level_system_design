class Student:
    def __init__(self,name,age,sub):
        self.name=name
        self.age=age
        self.sub=sub
    def display(self):
        print(f"student name is {self.name} and age is {self.age} and sub is {self.sub}")
s1=Student("rohan",34,"sci")
s2=Student("ashish",23,"math")
s1.display()
s2.display()