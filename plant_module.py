from db_connection import get_connection


def add_plant():
    connection = get_connection()

    if connection is None:
        return

    try:
        plant_id = int(input("Enter Plant ID: "))
        plant_name = input("Enter Plant Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        supplier_name = input("Enter Supplier Name: ")

        cursor = connection.cursor()

        query = """
        INSERT INTO plants
        (plant_id, plant_name, category, price, quantity, supplier_name)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            plant_id,
            plant_name,
            category,
            price,
            quantity,
            supplier_name
        )

        cursor.execute(query, values)
        connection.commit()

        print("\nPlant added successfully!")

    except ValueError:
        print("\nPlease enter valid numeric values.")

    except Exception as error:
        print("\nError:", error)

    finally:
        if connection:
            connection.close()


def view_plants():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM plants"
        cursor.execute(query)

        plants = cursor.fetchall()

        if not plants:
            print("\nNo plants found.")
            return

        print("\n---------------- PLANT LIST ----------------")
        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Category':<15}"
            f"{'Price':<10}"
            f"{'Quantity':<10}"
            f"{'Supplier':<20}"
        )
        print("-" * 83)

        for plant in plants:
            print(
                f"{plant[0]:<8}"
                f"{plant[1]:<20}"
                f"{plant[2]:<15}"
                f"{plant[3]:<10}"
                f"{plant[4]:<10}"
                f"{plant[5]:<20}"
            )

    except Exception as error:
        print("\nError:", error)

    finally:
        if connection:
            connection.close()


def update_plant():
    connection = get_connection()

    if connection is None:
        return

    try:
        plant_id = int(input("Enter Plant ID to update: "))

        cursor = connection.cursor()

        check_query = "SELECT * FROM plants WHERE plant_id = %s"
        cursor.execute(check_query, (plant_id,))

        plant = cursor.fetchone()

        if not plant:
            print("\nPlant not found.")
            return

        print("\nWhat do you want to update?")
        print("1. Plant Name")
        print("2. Category")
        print("3. Price")
        print("4. Quantity")
        print("5. Supplier Name")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter new plant name: ")
            query = "UPDATE plants SET plant_name = %s WHERE plant_id = %s"

        elif choice == "2":
            value = input("Enter new category: ")
            query = "UPDATE plants SET category = %s WHERE plant_id = %s"

        elif choice == "3":
            value = float(input("Enter new price: "))
            query = "UPDATE plants SET price = %s WHERE plant_id = %s"

        elif choice == "4":
            value = int(input("Enter new quantity: "))
            query = "UPDATE plants SET quantity = %s WHERE plant_id = %s"

        elif choice == "5":
            value = input("Enter new supplier name: ")
            query = "UPDATE plants SET supplier_name = %s WHERE plant_id = %s"

        else:
            print("\nInvalid choice.")
            return

        cursor.execute(query, (value, plant_id))
        connection.commit()

        print("\nPlant updated successfully!")

    except ValueError:
        print("\nPlease enter a valid value.")

    except Exception as error:
        print("\nError:", error)

    finally:
        if connection:
            connection.close()


def delete_plant():
    connection = get_connection()

    if connection is None:
        return

    try:
        plant_id = int(input("Enter Plant ID to delete: "))

        cursor = connection.cursor()

        check_query = "SELECT * FROM plants WHERE plant_id = %s"
        cursor.execute(check_query, (plant_id,))

        plant = cursor.fetchone()

        if not plant:
            print("\nPlant not found.")
            return

        confirm = input("Are you sure you want to delete this plant? (yes/no): ")

        if confirm.lower() == "yes":
            query = "DELETE FROM plants WHERE plant_id = %s"
            cursor.execute(query, (plant_id,))
            connection.commit()

            print("\nPlant deleted successfully!")

        else:
            print("\nDelete operation cancelled.")

    except ValueError:
        print("\nPlease enter a valid Plant ID.")

    except Exception as error:
        print("\nError:", error)

    finally:
        if connection:
            connection.close()


def search_plant():
    connection = get_connection()

    if connection is None:
        return

    try:
        search_name = input("Enter plant name to search: ")

        cursor = connection.cursor()

        query = """
        SELECT * FROM plants
        WHERE plant_name LIKE %s
        """

        cursor.execute(query, ("%" + search_name + "%",))

        plants = cursor.fetchall()

        if not plants:
            print("\nNo matching plants found.")
            return

        print("\n------------- SEARCH RESULTS -------------")

        for plant in plants:
            print(f"""
Plant ID      : {plant[0]}
Plant Name    : {plant[1]}
Category      : {plant[2]}
Price         : {plant[3]}
Quantity      : {plant[4]}
Supplier      : {plant[5]}
--------------------------------------------
""")

    except Exception as error:
        print("\nError:", error)

    finally:
        if connection:
            connection.close()


def plant_menu():
    while True:
        print("\n================================")
        print("        PLANT MODULE")
        print("================================")
        print("1. Add Plant")
        print("2. View Plants")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("5. Search Plant")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_plant()

        elif choice == "2":
            view_plants()

        elif choice == "3":
            update_plant()

        elif choice == "4":
            delete_plant()

        elif choice == "5":
            search_plant()

        elif choice == "6":
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    plant_menu()