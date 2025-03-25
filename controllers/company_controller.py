from classes.sql_connection import SQL_Connection
import MySQLdb

class CompanyController:
	def __init__(self):
		self.db = SQL_Connection()

	def add_company(self, name, user_id):
		query = "INSERT INTO companies (name, user_id) VALUES (%s, %s)"
		try:
			self.db.execute_query(query, (name, user_id))
			print(f"Successfully added company: {name}")
		except MySQLdb.Error as e:
			print(f"Error executing query: {e}")

	def get_all_companies(self):
		query = "SELECT * FROM companies"
		results = self.db.fetch_query(query)
		return [{"company_id": row[0], "name": row[1]} for row in results]