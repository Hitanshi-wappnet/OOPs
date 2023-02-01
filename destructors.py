class Employee:
    def __init__(self):
        print("Employee Object is created")

    def __del__(self):
        print("Object Employee is destroid")

    def greet(self):
        print("Good Evening Employee")

class Student:
    def __init__(self):
        print("Welcome to the class Students")

    def __del__(self):
        print("The student class is going to die")

Amita=Employee()
Amita.greet()
s=Student()