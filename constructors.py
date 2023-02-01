class student:

    #Non Parameterized Constructor
    def __init__(self):
        print("Welcome to the class")

    #Parameterized Constructor
    def __init__(self,name,id):
        self.sname=name
        self.rollno=id

    def display(self):
        print("The name of the student is",self.sname)
        print("The name of the student is",self.rollno)


#s1=student()
s1=student("Hitanshi",59)
s1.display()
