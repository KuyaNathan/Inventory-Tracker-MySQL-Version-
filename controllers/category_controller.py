from classes.sql_connection import SQL_Connection

class CategoryController:
	def __init__(self):
		self.db = SQL_Connection()

	def add_category(self, name, company_id):
		query = "INSERT INTO categories (name, company_id) VALUES (%s, %s)"
		self.db.execute_query(query, (name, company_id))
		print(f"Category '{name}' added for company ID {company_id}.")

	def remove_category(self, category_id):
		query = "DELETE FROM categories WHERE category_id = %s"
		self.db.execute_query(query, (category_id,))
		print(f"Category with ID {category_id} has been removed")

	def get_all_categories(self, company_id):
		query = "SELECT category_id, name FROM categories WHERE company_id = %s"
		results = self.db.fetch_query(query, (company_id,))
		return [{"category_id": row[0], "name": row[1]} for row in results]