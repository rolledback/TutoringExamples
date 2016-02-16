import random

class Wheel(object):
    # init a wheel, all wheels start at a random pressure between 0 and the maximum pressure
    def __init__(self, maxPressure):
        self.pressure = random.uniform(0, maxPressure)
        self.maxPressure = maxPressure

    # returns the current pressure
    def checkPressure(self):
        return self.pressure

    # change the current pressure by p, but don't go below 0 or above the wheel's limit
    def changePressure(self, p):
        self.pressure += p
        if self.pressure < 0:
            self.pressure = 0
        if self.pressure > self.maxPressure:
            self.pressure = self.maxPressure

class Vehicle(object):
    # init a Vehicle with the given number of wheels
    def __init__(self, maxWheelPressure, numWheels):
        self.wheels = []
        for i in range(numWheels):
            self.wheels.append(Wheel(maxWheelPressure))

class Car(Vehicle):
    # init a Car with the given number of wheels
    def __init__(self, make, model, year, numWheels, maxWheelPressure):
        Vehicle.__init__(self, maxWheelPressure, numWheels)
        self.make = make
        self.model = model
        self.year = year

    # drives the car by simulating a loss in tire pressure, pressure lost = (distance / 1000) * (44 / 7)^2
    def driveCar(self, distance):
        lostPressure = ((distance / 1000) * (44 / 7) ** 2) * -1
        for i in range(len(self.wheels)):
            self.wheels[i].changePressure(lostPressure)

def main():
    # make a 2014 Ford Focus, it has 4 wheels, each of which has a maximum pressure of 1500 PSI
    fordFocus = Car("Ford", "Focus", 2014, 4, 1500)

    # drive the car 5000 miles
    fordFocus.driveCar(5000)

    # print out the pressure in each tire
    for tire in fordFocus.wheels:
        print(tire.pressure)

main()
