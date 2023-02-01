class Person:
    name="Hitanshi"
    def getname(self):
        print("The name of the Person is",self.name)

class Programmer:
    technology="Java"
    def gettech(self):
        print("the technology of the Programmer is ",self.technology)

class Employee(Person,Programmer):
    salary=45000
    def getsalary(self):
        print("The salary of the Employee is ",self.salary)

p=Programmer()
e=Employee()
print(f"The name is {e.name} \nThe Technology is {e.technology} \nThe salary is {e.salary}")
e.getname()
e.gettech()
e.getsalary()
print(issubclass(Employee,Person))
print(issubclass(Programmer,Person))