class Person:
    def __init__(self):
        print("This is a person class")

    def __init__(self,id,name):
        self.id=id
        self.name=name

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("This is Employee class")

    def __init__(self,id,name):
        self.id=id

E=Employee(1,"xyz")
print(E.id)