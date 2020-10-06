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

carDb = database()
carDb.loadJsonFile('car_db.json')

print(carDb.getDict()[1].getMaxPayloadCapacity())
carDb.getCarsSortedByParameter("age", "descend")
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



#print("car dict:")
#print(myCar.__dict__['brand'])

#carDb.getCarsSortedByParameter("age", "descend")
#carDb.getCarsSortedByParameter("age", "asCend")
#carDb.getCarsSortedByParameter("Payload Capacity", "ascend")
#carDb.getCarsSortedByParameter("MAX SPEED", "asCend")

#carList = [myCar, mySecondCar, myThirdCar, myFourthCar]
#carDb.filterCarsByProductionDate(carList)