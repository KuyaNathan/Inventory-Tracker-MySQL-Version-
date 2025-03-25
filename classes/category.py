from classes.item import Item

class Category():
	def __init__(self, name, items = None):
		self.name = name
		if items is None:
			items = []
		self.items = items
