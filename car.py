import logging
import datetime
import json


class Car():
	id = 0

	def __init__(self):
		self.id = Car.id
		Car.id = Car.id + 1
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

    def datetimeConverter(self):
        if isinstance(self, datetime.datetime):
            return self.__str__()

    def logDataToConsole(self):
        print("===========================")
        print("id: " + str(self.getId()))
        print("brand: " + str(self.getBrand()))
        print("class: " + str(self.getCarType()))


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
        logging.info(" carType: " +
                     str(self.carType))
        logging.info(" maxPayloadCapacity: " +
                     str(self.maxPayloadCapacity))

    # def convertToJson(self):
    #    jsonStrPickUp = json.dumps(PickUp.__dict__)
    #    return jsonStrPickUp


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
        logging.info(" carType: " +
                     str(self.carType))
        logging.info(" maxSpeed: " +
                     str(self.maxSpeed))

    # def convertToJson(self):
    #        jsonStrSportsCar = json.dumps(SportsCar.__dict__)
    #        return jsonStrSportsCar
