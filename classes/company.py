from classes.category import Category
from classes.item import Item
from classes.order import Order

class Company():
	def __init__(self, name):
		self.name = name
		self.inventory = []
		self.orders = []
'''
	def changeName(self, new_name):
		self.name = new_name


	def checkIfCategoryExists(self, category_name):
		if any(Category.getName == category_name for category in self.inventory):
			return True
		else:
			return False
		
	def checkIfItemExists(self, item_name):
		for category in self.inventory:
			if any(Item.getName == item_name for item in category.getAllItems()):
				return True
		else:
			return False
	
	def addCategory(self, category):
		if self.checkIfCategoryExists(category.getName()) == False:
			self.inventory.append(category)
		else:
			raise Exception(f"Category named: {category.getName()} already exists")

	def addItem(self, item, category):
		if self.checkIfItemExists(item.getName()) == False:
			category.addItem(item)
		else:
			raise Exception(f"Item named: {item.getName()} already exists in category: {category.getName()}")

	def getName(self):
		return self.name
	
	def displayCompanyName(self):
		print(f"\nInventory for: {self.name} Company")
	
	def displayCategories(self):
		print(f"\nAll Item Categories for: {self.name} company")
		for category in self.inventory:
			if not None:
				print(f"- {category.getName()}")

	def displayItemsInCategory(self, category):
		print(f"\nAll Items in {category.getName()}")
		for item in category.getAllItems():
			print(f"* {item.getName()}")

	def placeOrder(self, item, order):
		if self.checkIfItemExists(item) == True:
			self.orders.append(order)
		else:
			raise Exception(f"")
'''	