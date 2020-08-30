import logging

class Car:
	def __init__(self, id):
		self.id = id
		self.logger = logging.debug("New ID added")

	def brand(self, brand):
		self.brand = brand
	

class PickUp(Car):
	def type(self, type):
		self.type = type

	def maxPayloadCapacity(self, maxPayloadCapacity):
		self.maxPayloadCapacity = maxPayloadCapacity

	def get_maxPayloadCapacity(self):
		return self.maxPayloadCapacity

class SportsCar(Car):
	def type(self, type):
		self.type = type

	def maxSpeed(self, maxSpeed):
		self.maxSpeed = maxSpeed

	def get_maxSpeed(self):
		return self.maxSpeed