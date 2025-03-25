import bcrypt
from classes.sql_connection import SQL_Connection
from classes.user import User
import MySQLdb

class UserController:
	def __init__(self):
		self.db = SQL_Connection()

	def register_user(self, username, password):
		# create hash of password to encrypt
		password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
		try:
			self.db.execute_query(query, (username, password_hash))
			print(f"Successfully registered user: {username}")
		except MySQLdb.IntegrityError:
			print(f"User with username: {username} already exists. Please enter a different name.")
		
	def authenticate_user(self, username, password):
		query = "SELECT user_id, username, password_hash FROM users WHERE username = %s"
		result = self.db.fetch_query(query, (username,))

		if result:
			user_id, username, password_hash = result[0]
			user = User(user_id, username, password_hash)
			if user.check_password(password):
				return user
		return None
	
	def get_user_companies(self, user_id):
		query = "SELECT * FROM companies WHERE user_id = %s"
		results = self.db.fetch_query(query, (user_id,))
		return [{'company_id': row[0], 'name': row[1]} for row in results]
	
	def get_user_categories(self, user_id):
		query = """
			SELECT cat.*
			FROM categories cat
			JOIN companies co ON cat.company_id = co.company_id
			WHERE co.user_id = %s
		"""
		results = self.db.fetch_query(query, (user_id,))
		return [{"category_id": row[0], "name": row[1]} for row in results]
	
	def get_user_items(self, user_id):
		query = """
			SELECT i.*
			FROM items i
			JOIN categories cat ON i.category_id = cat.category_id
			JOIN companies co ON cat.company_id = co.company_id
			WHERE co.user_id = %s
		"""
		results = self.db.fetch_query(query, (user_id,))
		return [{"item_id": row[0], "name": row[1], "price": row[2], "quantity": row[3], "category_id": row[4]} for row in results]