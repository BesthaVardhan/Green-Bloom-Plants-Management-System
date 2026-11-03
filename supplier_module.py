from db_connection import get_connection


# ADD SUPPLIER
def add_supplier():
    connection = get_connection()

    if connection is None:
        return

    try:
        supplier_id = input("Enter Supplier ID: ")
        supplier_name = input("Enter Supplier Name: ")
        phone = input("Enter Phone Number: ")
        city = input("Enter City: ")

        cursor = connection.cursor()

        query = """
        INSERT INTO suppliers
        (supplier_id, supplier_name, phone, city)
        VALUES (%s, %s, %s, %s)
        """

        values = (supplier_id, supplier_name, phone, city)

        cursor.execute(query, values)
        connection.commit()

        print("\nSupplier added successfully!")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# VIEW SUPPLIERS
def view_suppliers():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM suppliers"
        cursor.execute(query)

        suppliers = cursor.fetchall()

        if not suppliers:
            print("\nNo suppliers found.")
            return

        print("\n------------- SUPPLIERS -------------")

        for supplier in suppliers:
            print(f"""
Supplier ID   : {supplier[0]}
Supplier Name : {supplier[1]}
Phone         : {supplier[2]}
City          : {supplier[3]}
---------------------------------------
""")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# UPDATE SUPPLIER
def update_supplier():
    connection = get_connection()

    if connection is None:
        return

    try:
        supplier_id = input("Enter Supplier ID to update: ")

        cursor = connection.cursor()

        query = """
        SELECT * FROM suppliers
        WHERE supplier_id = %s
        """

        cursor.execute(query, (supplier_id,))
        supplier = cursor.fetchone()

        if not supplier:
            print("\nSupplier not found.")
            return

        print("\n1. Update Supplier Name")
        print("2. Update Phone")
        print("3. Update City")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_value = input("Enter new supplier name: ")

            query = """
            UPDATE suppliers
            SET supplier_name = %s
            WHERE supplier_id = %s
            """

        elif choice == "2":
            new_value = input("Enter new phone number: ")

            query = """
            UPDATE suppliers
            SET phone = %s
            WHERE supplier_id = %s
            """

        elif choice == "3":
            new_value = input("Enter new city: ")

            query = """
            UPDATE suppliers
            SET city = %s
            WHERE supplier_id = %s
            """

        else:
            print("\nInvalid choice.")
            return

        cursor.execute(query, (new_value, supplier_id))
        connection.commit()

        print("\nSupplier updated successfully!")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# DELETE SUPPLIER
def delete_supplier():
    connection = get_connection()

    if connection is None:
        return

    try:
        supplier_id = input("Enter Supplier ID to delete: ")

        cursor = connection.cursor()

        query = """
        SELECT * FROM suppliers
        WHERE supplier_id = %s
        """

        cursor.execute(query, (supplier_id,))
        supplier = cursor.fetchone()

        if not supplier:
            print("\nSupplier not found.")
            return

        confirm = input(
            "Are you sure you want to delete this supplier? (yes/no): "
        )

        if confirm.lower() == "yes":

            query = """
            DELETE FROM suppliers
            WHERE supplier_id = %s
            """

            cursor.execute(query, (supplier_id,))
            connection.commit()

            print("\nSupplier deleted successfully!")

        else:
            print("\nDelete operation cancelled.")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# SUPPLIER MENU
def supplier_menu():

    while True:

        print("\n================================")
        print("       SUPPLIER MODULE")
        print("================================")

        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Update Supplier")
        print("4. Delete Supplier")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_supplier()

        elif choice == "2":
            view_suppliers()

        elif choice == "3":
            update_supplier()

        elif choice == "4":
            delete_supplier()

        elif choice == "5":
            break

        else:
            print("\nInvalid choice. Please try again.")


# RUN SUPPLIER MODULE
if __name__ == "__main__":
    supplier_menu()