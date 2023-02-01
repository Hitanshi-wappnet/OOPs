class Employee:
    name="Hitanshi"
    age="21"
    def basicinfo(self):
        print("The name and age of the person is ",self.name ,"and" ,self.age)

class Programmer(Employee):
    salary="45k"
    language="Python"
    def details(self):
        print(f"The salary of the Programmer {self.name} is {self.salary}")
        print(f"{self.name} is working on  {self.language}")

class Manager(Programmer):
    mname="Jennifer"
    post="manager"
    def getinfo(self):
        print(f"The manager of {self.name} is {self.mname} and language working on is {self.language}")

m1=Manager()
m1.basicinfo()
m1.details()
m1.getinfo()
p=Programmer()
print(p.name)
print(m1.language)