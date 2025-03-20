from classes.sql_connection import SQL_Connection

class ItemController:
	def __init__(self):
		self.db = SQL_Connection()

	def add_item(self, name, price, quantity, category_id):
		query = "INSERT INTO items (name, price, quantity, category_id) VALUES (%s, %s, %s, %s)"
		self.db.execute_query(query, (name, price, quantity, category_id))
		print(f"Item '{name}' added successfully.")

	def remove_item(self, item_id):
		query = "DELETE FROM items WHERE item_id = %s"
		self.db.execute_query(query, (item_id,))
		print(f"Item with ID {item_id} has been removed")

	def increase_item_quantity(self, item_id, increase_amount):
		query = """
		UPDATE items
		SET quantity = quantity + %s
		WHERE item_id = %s
		"""
		self.db.execute_query(query, (increase_amount, item_id,))
		print(f"Increased item with ID {item_id} quantity by: {increase_amount}")

	def decrease_item_quantity(self, item_id, decrease_amount):
		query = """
		UPDATE items
		SET quantity = quantity - %s
		WHERE item_id = %s
		"""
		self.db.execute_query(query, (decrease_amount, item_id,))
		print(f"Decreased item with ID {item_id} quantity by: {decrease_amount}")

	def change_price(self, item_id, new_price):
		query= """
		UPDATE items
		SET price = %s
		WHERE item_id = %s
		"""
		self.db.execute_query(query, (new_price, item_id))
		print(f"Set new price of item with ID {item_id} to: {new_price}")

	def change_category(self, item_id, category_id):
		query = """
		UPDATE items
		SET category_id = %s
		WHERE item_id = %s
		"""
		self.db.execute_query(query, (category_id, item_id,))
		print(f"Changed category of Item with ID: {item_id} to Category with ID: {category_id}")

	def change_name(self, item_id, new_name):
		query = """
		UPDATE items
		SET name = %s
		WHERE item_id = %s
		"""
		self.db.execute_query(query, (new_name, item_id))
		print(f"Changed Name of Item with ID: {item_id} to: {new_name}")

	def get_all_items(self, company_id):
		query = """
		SELECT items.item_id, items.name, items.price, items.quantity, items.category_id 
    		FROM items
    		JOIN categories ON items.category_id = categories.category_id
    		WHERE categories.company_id = %s
		"""
		results = self.db.fetch_query(query, (company_id,))
		return [{"item_id": row[0], "name": row[1], "price": row[2], "quantity": row[3], "category_id": row[4]} for row in results]