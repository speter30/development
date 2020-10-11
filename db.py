from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
import car
from car import PickUp
from car import SportsCar
import json
from json import JSONEncoder

class database():

    def __init__(self):
        self.myDict = {}

    def loadJsonFile(self, file):
        #json beolvasás
        f = open(file)
        data = json.load(f)
        
        for i in data['cars']:
            if 'maxPayloadCapacity' in i:
                pickup = PickUp(i)
                self.addItem({pickup.getId() : pickup})

            elif 'maxSpeed' in i:
                sportcar = SportsCar(i)
                self.addItem({sportcar.getId() : sportcar})

            else:
                print('Unknown car type')

    def addItem(self, item):
        self.myDict.update(item)

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
        
        else:
            print("Misstyped parameters")


    def filterCarsByProductionDate(self, listOfObject):
        CarsByProductionDate = sorted(listOfObject, 
                                key = lambda x: x.getProductionDate(), 
                                reverse = True)
        
        for i in CarsByProductionDate:
            print(str(i.getProductionDate()) + " " + str(i.getBrand()) + " " 
                    + str(i.getCarType()) )

