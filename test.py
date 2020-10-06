from db import database
from car import Car
from car import PickUp
from car import SportsCar
from dateutil.relativedelta import relativedelta
import datetime

def test_example():
	myCar = PickUp(10)
	myCar.setBrand("Ford1")
	myCar.setCarType("F-150")
	myCar.setMaxPayloadCapacity(1640)
	myCar.setProductionDate(datetime.datetime(2015, 6, 8))
	

	#myCar.logData()
	
	mySecondCar = SportsCar(2)
	
	mySecondCar.setBrand("Audi")
	mySecondCar.setCarType("TT")
	mySecondCar.setMaxSpeed(280)
	mySecondCar.setProductionDate(datetime.datetime(2020, 9, 15))
	
	testDb = database()

	testDb.addItem({myCar.getBrand() : myCar})
	testDb.addItem({mySecondCar.getBrand() : mySecondCar})

	sortedList = testDb.carsByAge()
	print(sortedList)
	assert sortedList[0].getId() == 2
	#mySecondCar.logData()
	#
	#myThirdCar = PickUp(3)
	#
	#myThirdCar.setBrand("Ford2")
	#myThirdCar.setCarType("FD-100")
	#myThirdCar.setMaxPayloadCapacity(1056)
	#myThirdCar.setProductionDate(datetime.datetime(2013, 5, 10))
	#myThirdCar.logData()
	#
	#myFourthCar = PickUp(4)
	#
	#myFourthCar.setBrand("Toyota")
	#myFourthCar.setCarType("CD-500")
	#myFourthCar.setMaxPayloadCapacity(1050)
	#myFourthCar.setProductionDate(datetime.datetime(2010, 9, 13))
	#myFourthCar.logData()

def test_inputBrandValid():
	myCar = PickUp()
	myCar.setBrand("Ford")
	myCar.setCarType("F-150")
	myCar.setMaxPayloadCapacity(1640)
	myCar.setProductionDate(datetime.datetime(2015, 6, 8))
	
	mySecondCar = SportsCar()
		
	mySecondCar.setBrand("Audiaudiaudi")
	mySecondCar.setCarType("TT")
	mySecondCar.setMaxSpeed(280)
	mySecondCar.setProductionDate(datetime.datetime(2020, 9, 15))

	assert len(mySecondCar.getBrand()) < 10
	assert len(myCar.getBrand()) < 10

def test_loadJson_sortedByAge():
	carDb = database()
	carDb.loadJsonFile('car_db.json')
	result = carDb.getCarsSortedByParameter("age", "ascend")

	assert 4 == result[0].getId() 
