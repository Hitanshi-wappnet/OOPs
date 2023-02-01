class Parent:
    _a=30
    __d=80
    def __init__(self):
        self._b=50
        self.__e=80

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print(self._b)
        #print(self.__e)

    def getnum(self):
        print(self._a)
        #print(self.__d)
    _c=69

C1=Child()
print(C1._a)
print(C1._c)
#print(C1.__d)
C1.getnum()
print(C1._b)