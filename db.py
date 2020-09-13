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
			years = relativedelta(datetime.now(), c.getDate()).years

			if isinstance(c, car.PickUp) and years < 10:
				youngPickUps.append(c)

		return youngPickUps

	def carsByAge(self):

		cars = []
		for i in self.myDict:
			cars.append(self.myDict[i])

		# cars = [self.myDict[i] for i in self.myDict]

		cars.sort(key = lambda r: r.getDate())
		
		res = []
		for i in cars:
			res.append(i.getBrand())


		#res = [c.getBrand() for c in cars]

		return res