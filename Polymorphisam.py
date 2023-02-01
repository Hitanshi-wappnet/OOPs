class Bank:
    def deposit(self):
        print("The initial Deposit should be 1000")

class RBI:
    def deposit(self):
        print("The initial deposit should be zero")

class SBI(Bank):
    def deposit(self):
        print("The initial Deposit should be 500")

class Kalupur(Bank):
    def deposit(self):
        print("The initial Deposit should be 5000")

class ICI(Bank):
    def deposit(self):
        print("The initial Deposit should be 2000")

B=Bank()
S=SBI()
K=Kalupur()
I=ICI()
R=RBI()
R.deposit()

def fun(obj):
    obj.deposit()

fun(B)
fun(S)
fun(K)
fun(I)

def sum(a,b):
    s=a+b 
    print(s)
def sum(a,b,c):
    s=a+b+c
    print(s)
#sum(5,3)
sum(3,4,7)