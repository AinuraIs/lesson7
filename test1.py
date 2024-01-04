class Racer:
    def drive(self):
        print('xtnj')

class Car:
    def drive(self):
        print('плита')

class RacingCar(Car, Racer):
    pass

car = RacingCar()
car.drive()