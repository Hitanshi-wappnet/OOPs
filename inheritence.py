class person:
    def __init__(self,name,id):
        self.pname=name
        self.id=id

    def getdetails(self):
        print(f"The name of the Person is {self.pname}")
        print(f"The id of the Person is {self.id}")

class Employee(person):
    company="Wappnet"
    def gettech(self):
        Technology="python"
        print(f"The technology selected by {self.pname} is {Technology}")

e1=Employee("Hitanshi",1)
e1.getdetails()
e1.gettech()

