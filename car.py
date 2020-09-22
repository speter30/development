import logging
import datetime

class Car:
        def __init__(self, id):
                self.id = id
                self.logger = logging.debug("New ID added")

        def setBrand(self, brand):
                self.brand = brand

        def setProductionDate(self, date):
        		self.date = date

        def getId(self):
        	return self.id

        def getBrand(self):
        	return self.brand

        def getProductionDate(self):
        	return self.date

        def logData(self):
                logging.info(" === ")
                logging.info(" id: " + str(self.id))
                logging.info(" brand: " + str(self.brand))

class PickUp(Car):
        def setCarType(self, carType):
                self.carType = carType

        def setMaxPayloadCapacity(self, maxPayloadCapacity):
                self.maxPayloadCapacity = maxPayloadCapacity

        def getCarType(self):
        		return self.carType

        def getMaxPayloadCapacity(self):
                return self.maxPayloadCapacity

        def logData(self):
                super().logData()
                logging.info( " carType: " + 
                              str(self.carType))
                logging.info( " maxPayloadCapacity: " + 
                              str(self.maxPayloadCapacity))

class SportsCar(Car):
        def setCarType(self, carType):
                self.carType = carType

        def setMaxSpeed(self, maxSpeed):
                self.maxSpeed = maxSpeed

        def getMaxSpeed(self):
                return self.maxSpeed

        def getCarType(self):
        		return self.carType

        def logData(self):
                super().logData()
                logging.info( " carType: " + 
                              str(self.carType))
                logging.info( " maxSpeed: " + 
                              str(self.maxSpeed))

