from classes.item import Item

class Order():
	def __init__(self, item, quantity):
		self.item = item
		self.quantity = quantity
		self.total = item.getPrice() * quantity

	def verifyPurchase(self, item, avail_balance):
		if avail_balance >= self.total and item.getQuantity() >= self.quantity:
			item.removeQuantity(self.quantity)
		else:
			raise Exception(f"Cannot fulfill order: Insufficient funds or stock")
