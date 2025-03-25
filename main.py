from controllers.company_controller import CompanyController
from controllers.category_controller import CategoryController
from controllers.item_controller import ItemController
from controllers.user_controller import UserController
from classes.sql_connection import SQL_Connection
from classes.cmd_line_dashboard import cmd_line_user_dashboard
import MySQLdb

sql_connection = SQL_Connection()
sql_connection.initialize_db()

company_controller = CompanyController()
category_controller = CategoryController()
item_controller = ItemController()
user_controller = UserController()


def main_menu():
    print("\n-----Inventory Management System-----")
    print("Select an option:")
    
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("\nEnter you choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_controller.authenticate_user(username, password)

            if user:
                print("\nSuccessfully logged in!")
                cmd_line_user_dashboard(user)
            else:
                print("Invalid username or password")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_controller.register_user(username, password)
            print("Successfully registered. Please log in.")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
