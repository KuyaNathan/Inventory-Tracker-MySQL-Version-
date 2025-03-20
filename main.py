from controllers.company_controller import CompanyController
from controllers.category_controller import CategoryController
from controllers.item_controller import ItemController
from classes.sql_connection import SQL_Connection

sql_connection = SQL_Connection()
sql_connection.initialize_db()

company_controller = CompanyController()
category_controller = CategoryController()
item_controller = ItemController()


def main_menu():
    print("\n-----Inventory Management System-----")
    print("\nWelcome to the inventory tracker!")

    while True:
        print("\nWould you like to:")
        print("1. Select a company whose inventory to manage")
        print("2. Add a Company")
        print("3. View registered Companies")
        print("4. Exit")

        first_choice = input("Enter choice:")

        if first_choice == "1":
            print("\nSelect a registered company:")
            companies = company_controller.get_all_companies()
            if not companies:
                print("---No companies currently registered. Please add a company first---")
                continue

            print("---Available Companies---")
            for i, company in enumerate(companies, start=1):
                print(f"{i}. {company['name']} (ID: {company['company_id']})")

            try:
                company_choice = int(input("Enter your choice (number): ")) - 1
                if company_choice < 0 or company_choice >= len(companies):
                    print("\nInvalid choice")
                    continue
                selected_company = companies[company_choice]
                selected_company_id = selected_company["company_id"]
                print(f"\nManaging inventory for {selected_company['name']}\n")
            except ValueError:
                print("Invalid input")
                continue


            while True:
                print("\n1. Add Category")
                print("2. Remove Category")
                print("3. View Categories")
                print("4. Add Item")
                print("5. Remove Item")
                print("6. Update Item")
                print("7. View Items")
                print("8. Exit")

                choice = input("Enter choice: ")

                if choice == "1": # add category
                    name = input("\nEnter category name: ")
                    category_controller.add_category(name, selected_company_id)

                elif choice == "2": # remove category
                    categories = category_controller.get_all_categories(selected_company_id)
                    if not categories:
                        print("\n---No categories found to remove---")
                        continue
                    
                    print("\nSelect a Category to remove (NOTE: All Items within the category will also be removed)")
                    print("---Available Categories---")
                    for i, category in enumerate(categories, start=1):
                        print(f"{i}. {category['name']} (ID: {category['category_id']})")
                    print("\nEnter an invalid choice to Exit / Cancel")

                    try:
                        category_choice = int(input("Select category to remove/delete(number): ")) - 1
                        if category_choice < 0 or category_choice >= len(categories):
                            print("\nInvalid choice")
                            continue
                        category_id = categories[category_choice]["category_id"]
                        category_controller.remove_category(category_id)
                    except ValueError:
                        print("Invalid input.")

                elif choice == "3": # view categories
                    categories = category_controller.get_all_categories(selected_company_id)
                    if categories:
                        print(f"\n---Categories for {selected_company['name']}---")
                        for category in categories:
                            print(f"- {category['name']} (ID: {category['category_id']})")
                    else:
                        print("\n---No categories found for this company---")

                elif choice == "4": # add item
                    name = input("\nEnter item name: ")
                    price = float(input("Enter price (In decimal form): "))
                    quantity = int(input("Enter quantity: "))

                    categories = category_controller.get_all_categories(selected_company_id)
                    if not categories:
                        print("\n---No categories found for this company. Add a category first---")
                        continue
                    
                    print("\nSelect the category that the item belongs in:")
                    print("---Available Categories---")
                    for i, category in enumerate(categories, start=1):
                        print(f"{i}. {category['name']} (ID: {category['category_id']})")

                    try:
                        category_choice = int(input("\nSelect category (number): ")) - 1
                        if category_choice < 0 or category_choice >= len(categories):
                            print("\nInvalid choice")
                            continue
                        category_id = categories[category_choice]["category_id"]
                    except ValueError:
                        print("\nInvalid input")
                        continue

                    item_controller.add_item(name, price, quantity, category_id)

                elif choice == "5": # remove item
                    items = item_controller.get_all_items(selected_company_id)
                    if not items:
                        print("\n---No items available to delete---")
                        continue

                    print("\nSelect an Item to remove:")
                    print("---Available Items---")
                    for i, item in enumerate(items, start=1):
                        print(f"{i}. {item['name']} (ID: {item['item_id']})")
                    print("Enter an invalid choice to Exit / Cancel")

                    try:
                        item_choice = int(input("\nSelect item to remove (number): ")) - 1
                        if item_choice < 0 or item_choice >= len(items):
                            print("\nInvalid choice")
                            continue
                        item_id = items[item_choice]["item_id"]
                        item_controller.remove_item(item_id)
                    except ValueError:
                        print("\nInvalid input")

                elif choice == "6": # update item
                    items = item_controller.get_all_items(selected_company_id)
                    if not items:
                        print("\n---No items available to update---")
                        continue
                    
                    print("\nSelect the item to be updated:")
                    print("---Available Items---")
                    for i, item in enumerate(items, start = 1):
                        print(f"{i}. {item['name']} (ID: {item['item_id']})")
                    print("Enter an invalid choice to Exit / Cancel")

                    try:
                        item_choice = int(input("\nSelect an item to update (number): ")) - 1
                        if item_choice < 0 or item_choice >= len(items):
                            print("\nInvalid choice")
                            continue
                        item_id = items[item_choice]["item_id"]
                        while True:
                            print("\nSelect how you would like to update the item:")
                            print("1. Update Quantity")
                            print("2. Update Price")
                            print("3. Update Category")
                            print("4. Update Name")
                            print("5. Cancel / Exit")

                            update_choice = input("\nEnter Choice: ")
                            if update_choice == "1":
                                print("\nWould you like to add Increase or Decrease quantity:")
                                print("1. Increase")
                                print("2. Decrease")
                                print("3. Cancel")
                                change_choice = input("\nEnter Choice: ")
                                if change_choice == "1":
                                    print("\nHow much would you like to add?")
                                    increase_amount = input("Enter amount: ")
                                    item_controller.increase_item_quantity(item_id, increase_amount)
                                elif change_choice == "2":
                                    print("\nHow much would you like to decrease?")
                                    decrease_amount = input("Enter amount: ")
                                    item_controller.decrease_item_quantity(item_id, decrease_amount)
                                elif change_choice == "3":
                                    continue
                                else:
                                    print("\nInvalid input")

                            elif update_choice == "2":
                                print("\nPlease enter the new Item Price")
                                new_price = input("Enter New Price: ")
                                item_controller.change_price(item_id, new_price)
                            
                            elif update_choice == "3":
                                print("\nSelect the Category in which you would like to move the Item to")
                                print("---Available Categories---")
                                categories = category_controller.get_all_categories(selected_company_id)
                                for i, category in enumerate(categories, start=1):
                                    print(f"{i}. {category['name']} (ID: {category['category_id']})")
                                print("Enter an invalid chouice to Exit / Cancel")

                                try:
                                    category_choice = int(input("\nSelect category (number): ")) - 1
                                    if (category_choice < 0 or category_choice >= len(categories)):
                                        print("\nInvalid choice.")
                                        continue
                                    category_id = categories[category_choice]["category_id"]
                                    item_controller.change_category(item_id, category_id)
                                except ValueError:
                                    print("\nInvalid input")
                                    continue

                            elif update_choice == "4":
                                print("\nEnter the New Name for the Item")
                                new_name = input("Enter New Name: ")
                                item_controller.change_name(item_id, new_name)

                            elif update_choice == "5":
                                break

                    except ValueError:
                        print("\nInvalid input")
                
                elif choice == "7": # view items
                    items = item_controller.get_all_items(selected_company_id)
                    if items:
                        print(f"\n---Items for {selected_company['name']}---")
                        for item in items:
                            print(f"- {item['name']} | Price: {item['price']} | Quantity: {item['quantity']} | Category ID: {item['category_id']}")
                    else:
                        print("\nNo items found for this company")

                elif choice == "8": # exit
                    break

        elif first_choice == "2":
            name = input("\nEnter company name: ")
            company_controller.add_company(name)

        elif first_choice == "3":
            print("\n---Registered Companies---")
            companies = company_controller.get_all_companies()
            for company in companies:
                print(company)

        elif first_choice == "4":
            break

        else:
            print("\nInvalid input, please try again.")