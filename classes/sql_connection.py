import os
from dotenv import load_dotenv
import bcrypt
import MySQLdb

load_dotenv("db_config.env")

DB_CONFIG = {
	'host': os.getenv('DB_HOST'),
    	'user': os.getenv('DB_USER'),
    	'password': os.getenv('DB_PASSWORD'),
    	'database': os.getenv('DB_NAME')
}

class SQL_Connection():
	def __init__(self):
		self.connection = MySQLdb.connect(
			host = DB_CONFIG['host'],
			user = DB_CONFIG['user'],
			password = DB_CONFIG['password']
		)
		self.cursor = self.connection.cursor()
		self.initialize_db()

	def initialize_db(self):
		# creates the database if it doesnt already exist
		self.cursor.execute("CREATE DATABASE IF NOT EXISTS inventory_db")
		self.connection.select_db(DB_CONFIG['database'])

		# creates the tables if they do not already exist

		
		# users table for logging in
		self.cursor.execute(
			"""
				CREATE TABLE IF NOT EXISTS `users`(
					`user_id` INT NOT NULL AUTO_INCREMENT,
					`username` varchar(255) UNIQUE NOT NULL,
					`password_hash` varchar(255) NOT NULL,
					PRIMARY KEY (`user_id`)
				)
			"""
		)

		self.cursor.execute(
			"""
				CREATE TABLE IF NOT EXISTS `companies`(
					`company_id` INT NOT NULL AUTO_INCREMENT,
					`name` varchar(255) UNIQUE NOT NULL,
					`user_id` INT NOT NULL,
					PRIMARY KEY (`company_id`),
					KEY `FK_user_id` (`user_id`),
					CONSTRAINT `FK_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE
				)
			"""
		)

		self.cursor.execute(
			"""
				CREATE TABLE IF NOT EXISTS `categories`(
					`category_id` INT AUTO_INCREMENT,
					`name` varchar(255) UNIQUE NOT NULL,
					`company_id` INT NOT NULL,
					PRIMARY KEY (`category_id`),
					KEY `FK_company_id` (`company_id`),
					CONSTRAINT `FK_client_id` FOREIGN KEY (`company_id`) REFERENCES `companies` (`company_id`) ON DELETE CASCADE
				)
			"""
		)

		self.cursor.execute(
			"""
				CREATE TABLE IF NOT EXISTS `items`(
					`item_id` INT AUTO_INCREMENT,
					`name` varchar(255) UNIQUE NOT NULL,
					`price` DECIMAL(10,2) NOT NULL DEFAULT 0.00,
					`quantity` INT NOT NULL DEFAULT 0,
					`category_id` INT NOT NULL,
					PRIMARY KEY (`item_id`),
					KEY `FK_category_id` (`category_id`),
					CONSTRAINT `FK_category_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`) On DELETE CASCADE
				)
			"""
		)

		self.connection.commit()
	
	def execute_query(self, query, parameters = None):
		try:
			if parameters:
				self.cursor.execute(query, parameters)
			else:
				self.cursor.execute(query)
			self.connection.commit()
		except MySQLdb.Error as e:
			print(f"Error executing query: {e}")
	
	def fetch_query(self, query, parameters = None):
		self.execute_query(query, parameters)
		return self.cursor.fetchall()