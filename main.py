import logging
from car import Car
from car import PickUp
from car import SportsCar
from db import database


logging.basicConfig(filename='car_traces.log',
                    level=logging.INFO)
logging.info("The program has started")


myCar = PickUp(1)

myCar.setBrand("Ford")
myCar.setCarType("F-150")
myCar.setMaxPayloadCapacity(1640)
myCar.logData()

mySecondCar = SportsCar(2)

mySecondCar.setBrand("Audi")
mySecondCar.setCarType("TT")
mySecondCar.setMaxSpeed(280)
mySecondCar.logData()

#--------
carDb = database()

carDb.addItem({myCar.getBrand() : myCar})
carDb.addItem({mySecondCar.getBrand() : mySecondCar})

print(carDb.getDict()["Ford"].getMaxPayloadCapacity())

for i in carDb.getDict():
	print(i + " " + str(carDb.getDict()[i].getId()))