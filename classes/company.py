from classes.category import Category
from classes.item import Item
from classes.order import Order

class Company():
	def __init__(self, name):
		self.name = name
		self.inventory = []
		self.orders = []
