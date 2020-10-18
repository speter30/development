import logging
#import datetimeConverter
from datetime import datetime

class Car():

    def __init__(self, inputDict = None):
        if inputDict is None:
            id = -1
            self.logger = logging.debug("Car is not initialized")

        else:
            self.id = inputDict['id']
            self.brand = inputDict['brand']
            self.date = inputDict['date']
        self.logger = logging.debug("New ID added")

    def setBrand(self, brand):
        if len(brand) >= 10:
            self.brand = brand[0:9]
        else:
            self.brand = brand

    def setProductionDate(self, date):
        self.date = date

    def setId(self, identity):
        self.id = identity

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

    def datetimeConverter(self):
        if isinstance(self, datetime.datetime):
            return self.__str__()

    def logDataToConsole(self):
        print("===========================")
        print("id: " + str(self.getId()))
        print("brand: " + str(self.getBrand()))

class PickUp(Car):
    def __init__(self, inputDict = None):
        if inputDict is not None:
            Car.__init__(self, inputDict)
            self.carType = inputDict['type']
            self.maxPayloadCapacity = inputDict['maxPayloadCapacity']

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
        logging.info(" carType: " +
                     str(self.carType))
        logging.info(" maxPayloadCapacity: " +
                     str(self.maxPayloadCapacity))

class SportsCar(Car):
    def __init__(self, inputDict = None):
        if inputDict is not None:
            Car.__init__(self, inputDict)
            self.carType = inputDict['type']
            self.maxSpeed = inputDict['maxSpeed']

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
        logging.info(" carType: " +
                     str(self.carType))
        logging.info(" maxSpeed: " +
                     str(self.maxSpeed))