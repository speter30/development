from db import database
from car import Car
from car import PickUp
from car import SportsCar
from dateutil.relativedelta import relativedelta
import datetime

def test_example():
    testCarDb = database()
    testCarDb.loadJsonFile('car_db.json')

    assert testCarDb.getYoungPickUps()[2].getId() == 4

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

def test_loadJson_sortedByPayload():
    carDb = database()
    carDb.loadJsonFile('car_db.json')
    result = carDb.getCarsSortedByParameter("payload capacity", "descend")

    assert 1056 == result[1].getMaxPayloadCapacity()

def test_loadJson_sortedBySpeed():
    carDb = database()
    carDb.loadJsonFile('car_db.json')
    result = carDb.getCarsSortedByParameter("max speed", "ascend")

    assert 5 == result[1].getId()