from classes.sql_connection import SQL_Connection

class CompanyController:
	def __init__(self):
		self.db = SQL_Connection()

	def add_company(self, name):
		query = "INSERT INTO companies (name) VALUES (%s)"
		self.db.execute_query(query, (name,))

	def get_all_companies(self):
		query = "SELECT * FROM companies"
		results = self.db.fetch_query(query)
		return [{"company_id": row[0], "name": row[1]} for row in results]