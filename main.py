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

myCar = PickUp()

myCar.setBrand("Ford1")
myCar.setCarType("F-150")
myCar.setMaxPayloadCapacity(1640)
myCar.setProductionDate(datetime.datetime(2015, 6, 8))
myCar.logData()

mySecondCar = SportsCar()

mySecondCar.setBrand("Audi")
mySecondCar.setCarType("TT")
mySecondCar.setMaxSpeed(280)
mySecondCar.setProductionDate(datetime.datetime(2020, 9, 15))
mySecondCar.logData()

myThirdCar = PickUp()

myThirdCar.setBrand("Ford2")
myThirdCar.setCarType("FD-100")
myThirdCar.setMaxPayloadCapacity(1056)
myThirdCar.setProductionDate(datetime.datetime(2013, 5, 10))
myThirdCar.logData()

myFourthCar = PickUp()

myFourthCar.setBrand("Toyota")
myFourthCar.setCarType("CD-500")
myFourthCar.setMaxPayloadCapacity(1050)
myFourthCar.setProductionDate(datetime.datetime(2010, 9, 13))
myFourthCar.logData()

print(myCar.getId())
print(mySecondCar.getId())
print(myThirdCar.getId())
print(myFourthCar.getId())

#--------
carDb = database()

carDb.addItem({myCar.getBrand() : myCar})
carDb.addItem({mySecondCar.getBrand() : mySecondCar})
carDb.addItem({myThirdCar.getBrand() : myThirdCar})
carDb.addItem({myFourthCar.getBrand() : myFourthCar})

# print(carDb.getDict()["Ford1"].getMaxPayloadCapacity())
# 
# for i in carDb.getDict():
# 	print(i + " " + str(carDb.getDict()[i].getId()))
# 
# asd = carDb.getPickUpsByAge(10)
# for i in asd:
# 	logging.info(i.getBrand() + " " + str(i.getId()))
# 
# carDb.carsByAge()

#--------------

# json file feltöltése

#with open("car_db.json", "w") as write_file:
#	for i in carDb.getDict():
#		json.dump(carDb.getDict()[i].__dict__, write_file, default = json_util.default)

#json beolvasás
f = open('car_db.json',)
data = json.load(f)

# for i in data['cars']:
# 	print(i)
# 	for key, value in i.items():
# 		print("key: " + key)
# 		print("value: " + str(value))
	# asd = Car(i)
	# asd.logDataToConsole()
	# print(asd)

#print("car dict:")
#print(myCar.__dict__['brand'])

#carDb.getCarsSortedByParameter("age", "descend")
#carDb.getCarsSortedByParameter("age", "asCend")
#carDb.getCarsSortedByParameter("Payload Capacity", "ascend")
#carDb.getCarsSortedByParameter("MAX SPEED", "asCend")

#carList = [myCar, mySecondCar, myThirdCar, myFourthCar]
#carDb.filterCarsByProductionDate(carList)