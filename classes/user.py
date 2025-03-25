import bcrypt

class User:
	def __init__(self, user_id, username, password_hash):
		self.user_id = user_id
		self.username = username
		self.password_hash = password_hash

	def check_password(self, password):
		# checks if the entered password matches the hashed password that is stored
		return bcrypt.checkpw(password.encode(), self.password_hash.encode())