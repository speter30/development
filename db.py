from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
import car
from car import PickUp
from car import SportsCar
import json
import os

class database():

    def __init__(self):
        self.myDict = {}


    def loadJsonFile(self, file):
        #json beolvasás
        try:
            f = open(file)
        except OSError:
            print("database not found... exit")
            return -1

        data = json.load(f)

        invalidInputCounter = 0
        for i in data['cars']:
            try:
                self.validateInputFields(i)
            except KeyError:
                print("not valid input " + str(i))
                invalidInputCounter += 1
                continue

            if 'maxPayloadCapacity' in i:
                    pickup = PickUp(i)
                    self.addItem({pickup.getId() : pickup})

            elif 'maxSpeed' in i:
                    sportcar = SportsCar(i)
                    self.addItem({sportcar.getId() : sportcar})

            else:
                print('Unknown car type')

        return invalidInputCounter

    def addItem(self, item):
        self.myDict.update(item)

    def validateInputFields(self, item):
        print(type(item))
        print("validates: " + str(item))
        if not "brand" in item:
            print("brand not found")
        if not all(k in item for k in ('id','brand','carType','date')):
            print("validates2: " + str(item))
            raise KeyError

    def getDict(self):
        return self.myDict

    def getYoungPickUps(self):
        currentYear = datetime.now().year
        currentMonth = datetime.now().month
        youngPickUps = []

        for i in self.myDict:
            c = self.myDict[i]

            if isinstance(c, car.PickUp):
                if c.getProductionDate()[0] > currentYear - 10:
                    youngPickUps.append(c)

            if isinstance(c, car.PickUp): 
                if c.getProductionDate()[0] == currentYear - 10:
                    if c.getProductionDate()[1] < currentMonth:
                        youngPickUps.append(c)

        return youngPickUps

    def getCarsSortedByParameter(self, param, order):
        if param.lower() == "age":

            carsDate = []
            for i in self.myDict:
                carsDate.append(self.myDict[i])
            carsByAge = sorted(carsDate,
                            key = lambda x: x.getProductionDate(),
                            reverse = True if order.lower() == "descend" else False)

            for c in carsByAge:
                c.logData()
                print(str(c.getId()) + " " + str(c.getProductionDate()))

            return carsByAge

        elif param.lower() == "payload capacity":
            carsPayload = []
            
            for i in self.myDict:
                if isinstance(self.myDict[i], car.PickUp):
                    carsPayload.append(self.myDict[i])
            carsByPayloadCapacity = sorted(carsPayload, 
                                    key = lambda x: x.getMaxPayloadCapacity(),
                                    reverse = True if order.lower() == "descend" else False)

            for c in carsByPayloadCapacity:
                c.logData()
                print(str(c.getId()) + " " + str(c.getMaxPayloadCapacity()))

            return carsByPayloadCapacity

        elif param.lower() == "max speed":
            carsSpeed = []

            for i in self.myDict:
                if isinstance(self.myDict[i], car.SportsCar):
                    carsSpeed.append(self.myDict[i])
            carsBySpeed = sorted(carsSpeed, key = lambda x: x.getMaxSpeed(),
                            reverse = True if order.lower() == "descend" else False)

            for c in carsBySpeed:
                c.logData()
                print(str(c.getId()) + " " + str(c.getMaxSpeed()))

            return carsBySpeed
        else:
            print("Misstyped parameters")