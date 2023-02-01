class car():
    def speed():
        pass

class Tesla(car):
    def speed(self):
        print("The speed of the class is 100 kmh")

class Suzuki(car):
    def speed(self):
        print("The speed of the class is 60 kmh")

class I20(car):
    def speed(self):
        print("The speed of the class is 30 kmh")

T=Tesla()
T.speed()
S=Suzuki()
S.speed()
I=I20()
I.speed()