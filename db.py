from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
import car

class database():

	def __init__(self):
		self.myDict = {}

	def addItem(self, item):
		self.myDict.update(item)

	def getDict(self):
		return self.myDict

	def getPickUpsByAge(self, age):
		currentYear = datetime.now().year
		currentMonth = datetime.now().month
		youngPickUps = []

		for i in self.myDict:
			c = self.myDict[i]
			years = relativedelta(datetime.now(), c.getProductionDate()).years

			if isinstance(c, car.PickUp) and years < 10:
				youngPickUps.append(c)

		return youngPickUps

	def carsByAge(self):

		cars = []
		for i in self.myDict:
			cars.append(self.myDict[i])

		# cars = [self.myDict[i] for i in self.myDict]

		carListByAge = sorted(cars, key = lambda r: r.getId())

		#res = [c.getBrand() for c in cars]
		print(carListByAge)
		return carListByAge 

	def getCarsSortedByParameter(self, param, order):
		if param.lower() == "age": #and order.lower() == "descend":
			#currentYear = datetime.now().year
			#currentMonth = datetime.now().month
			
			carsDate = []
			for i in self.myDict:
				carsDate.append(self.myDict[i])
			carsByAge = sorted(carsDate,
							key = lambda x: x.getProductionDate(),
							reverse = True if order.lower() == "descend" else False)

			for c in carsByAge:
				c.logData()
				print(str(c.getId()) + " " + str(c.getProductionDate()))

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