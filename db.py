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
		if param == "age" and order == "descend":
			currentYear = datetime.now().year
			currentMonth = datetime.now().month
			
			carsDate = []
			for i in self.myDict:
				carsDate.append(self.myDict[i])
			carsByAge = sorted(carsDate, key = lambda x: x.getProductionDate(), reverse = True)

			print(carsByAge)

		if param == "age" and order == "ascend":
			currentYear = datetime.now().year
			currentMonth = datetime.now().month
			
			carsDate = []
			for i in self.myDict:
				carsDate.append(self.myDict[i])
			carsByAge = sorted(carsDate, key = lambda x: x.getProductionDate())

			print(carsByAge)
			