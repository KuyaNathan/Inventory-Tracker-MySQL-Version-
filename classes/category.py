from classes.item import Item

class Category():
	def __init__(self, name, items = None):
		self.name = name
		if items is None:
			items = []
		self.items = items
'''	
	def addItem(self, item):
		self.items.append(item)
	
	def removeItem(self, item):
		self.items.remove(item)

	def changeName(self, new_name):
		self.name = new_name

	def getName(self):
		return self.name
	
	def getItem(self, item_name):
		for item_name in self.items:
			return item_name
		
	def getAllItems(self):
		return self.items
'''