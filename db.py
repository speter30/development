from datetime import datetime

class database():

	def __init__(self):
		self.myDict = {}

	def addItem(self, item):
		self.myDict.update(item)

	def getDict(self):
		return self.myDict

	def newPickUps(self):
		currentYear = datetime.now().year
		for i in self:
		