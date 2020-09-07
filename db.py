class database():

	def __init__(self):
		self.myDict = {}

	def addItem(self, item):
		self.myDict.update(item)

	def getDict(self):
		return self.myDict

	