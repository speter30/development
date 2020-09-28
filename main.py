import logging
from car import Car
from car import PickUp
from car import SportsCar
from db import database
import datetime
import json
from bson import json_util

logging.basicConfig(filename='car_traces.log',
                    level=logging.INFO,
                    filemode='w')
logging.info("The program has started")

#x = datetime.datetime(2010, 5, 17)

myCar = PickUp(1)

myCar.setBrand("Ford1")
myCar.setCarType("F-150")
myCar.setMaxPayloadCapacity(1640)
myCar.setProductionDate(datetime.datetime(2015, 6, 8))
myCar.logData()

mySecondCar = SportsCar(2)

mySecondCar.setBrand("Audi")
mySecondCar.setCarType("TT")
mySecondCar.setMaxSpeed(280)
mySecondCar.setProductionDate(datetime.datetime(2020, 9, 15))
mySecondCar.logData()

myThirdCar = PickUp(3)

myThirdCar.setBrand("Ford2")
myThirdCar.setCarType("FD-100")
myThirdCar.setMaxPayloadCapacity(1056)
myThirdCar.setProductionDate(datetime.datetime(2013, 5, 10))
myThirdCar.logData()

myFourthCar = PickUp(4)

myFourthCar.setBrand("Toyota")
myFourthCar.setCarType("CD-500")
myFourthCar.setMaxPayloadCapacity(1050)
myFourthCar.setProductionDate(datetime.datetime(2010, 9, 13))
myFourthCar.logData()

#--------
carDb = database()

carDb.addItem({myCar.getBrand() : myCar})
carDb.addItem({mySecondCar.getBrand() : mySecondCar})
carDb.addItem({myThirdCar.getBrand() : myThirdCar})
carDb.addItem({myFourthCar.getBrand() : myFourthCar})

print(carDb.getDict()["Ford1"].getMaxPayloadCapacity())

for i in carDb.getDict():
	print(i + " " + str(carDb.getDict()[i].getId()))

asd = carDb.getPickUpsByAge(10)
for i in asd:
	logging.info(i.getBrand() + " " + str(i.getId()))

carDb.carsByAge()

#--------------


with open("car_db.json", "w") as write_file:
	for i in carDb.getDict():
		json.dump(carDb.getDict()[i].__dict__, write_file, default = json_util.default)

print("-------------")

#carDb.getCarsSortedByParameter("age", "descend")
#carDb.getCarsSortedByParameter("age", "asCend")
carDb.getCarsSortedByParameter("Payload Capacity", "ascend")
#carDb.getCarsSortedByParameter("MAX SPEED", "asCend")

carList = [myCar, mySecondCar, myThirdCar, myFourthCar]
carDb.filterCarsByProductionDate(carList)