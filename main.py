import logging
from car import Car
from car import PickUp
from car import SportsCar


logging.basicConfig(level=logging.INFO)
logging.info("The program has started")


myCar = PickUp(1)

myCar.brand("Ford")
myCar.type("F-150")
myCar.maxPayloadCapacity(1640)

print(myCar.id)
print(myCar.brand)
print(myCar.type)
print(myCar.get_maxPayloadCapacity())

mySecondCar = SportsCar(2)

mySecondCar.brand("Audi")
mySecondCar.type("TT")
mySecondCar.maxSpeed(280)

print(mySecondCar.id)
print(mySecondCar.brand)
print(mySecondCar.type)
print(mySecondCar.get_maxSpeed())

