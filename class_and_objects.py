class Person:

    company="Wappnet"
    doj="23/01/2023"

    def __init__(self,name,number):
        self.P_name=name
        self.enroll_no=number

    def getdetails(self):
        print("The name of the employee is",self.P_name)
        print("The enrollment number of the employee is",self.enroll_no)


Employee=Person("Hitanshi",108)
Employee.getdetails()
print(f"the company name of the Employee is {Person.company} and Date of joining is {Person.doj}")

