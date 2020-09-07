import logging
from car import Car
from car import PickUp
from car import SportsCar


logging.basicConfig(filename='car_traces.log',
                    level=logging.INFO)
logging.info("The program has started")


myCar = PickUp(1)

myCar.brand("Ford")
myCar.setCarType("F-150")
myCar.setMaxPayloadCapacity(1640)
myCar.logData()

mySecondCar = SportsCar(2)

mySecondCar.brand("Audi")
mySecondCar.setCarType("TT")
mySecondCar.setMaxSpeed(280)
mySecondCar.logData()

