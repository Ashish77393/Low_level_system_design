class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("animal is speak")
    # polymorphisma method overiding
    def Move(self):
        print("all animals are moving ")
class Dog(Animal):
    def __init__(self, name:str, age:int,breed:str):
        super().__init__(name, age)
        self.breed=breed
    def eat(self):
        print(f"dog is eat ans its name is {self.name} and age is {self.age} and breed is {self.breed}")
    # polymorphisma method overiding
    def Move(self):
        print("all dogs are move towards roads")
D=Dog("tiger",10,"llcn")
D.eat()
D.Move()
D.speak()
a=Animal("saga",12)
a.speak()
a.Move()