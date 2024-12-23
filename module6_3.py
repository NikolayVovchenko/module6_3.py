from AppData.Local.Programs.Python.Python312.Lib.random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords =[0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print('It`s too deep, i can`t dive :')
        else:
            self._cords[0]  += dx * self.speed
            self._cords[1]  += dy * self.speed
            self._cords[2]  += dz * self.speed

    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Soory, i`m peaceful :')
        else:
            print('Be careful, i`m attacting you 0_0')

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is){randint(1, 4)} edds for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed // 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):

    def __init__(self, speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'

db = Duckbill(10)
print('----------------------------------')
print(db.live)
print(db.beak)
print('----------------------------------')
db.speak()
db.attack()
print('-----------------------------------')
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
print('-----------------------------------')