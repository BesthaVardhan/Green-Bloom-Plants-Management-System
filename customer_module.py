from db_connection import get_connection


# -----------------------------------------
# ADD CUSTOMER
# -----------------------------------------
def add_customer():
    connection = get_connection()

    if connection is None:
        return

    try:
        customer_id = int(input("Enter Customer ID: "))
        customer_name = input("Enter Customer Name: ")
        phone = input("Enter Phone Number: ")
        city = input("Enter City: ")

        cursor = connection.cursor()

        query = """
        INSERT INTO customers
        (customer_id, customer_name, phone, city)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            customer_id,
            customer_name,
            phone,
            city
        )

        cursor.execute(query, values)
        connection.commit()

        print("\nCustomer added successfully!")

    except ValueError:
        print("\nCustomer ID must be a number.")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# -----------------------------------------
# VIEW CUSTOMERS
# -----------------------------------------
def view_customers():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM customers"

        cursor.execute(query)

        customers = cursor.fetchall()

        if not customers:
            print("\nNo customers found.")
            return

        print("\n------------- CUSTOMER LIST -------------")

        for customer in customers:
            print(f"""
Customer ID   : {customer[0]}
Customer Name : {customer[1]}
Phone         : {customer[2]}
City          : {customer[3]}
-------------------------------------------
""")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# -----------------------------------------
# CUSTOMER PURCHASE HISTORY
# -----------------------------------------
def customer_purchase_history():
    connection = get_connection()

    if connection is None:
        return

    try:
        customer_id = int(input("Enter Customer ID: "))

        cursor = connection.cursor()

        # First get the customer name
        customer_query = """
        SELECT customer_name
        FROM customers
        WHERE customer_id = %s
        """

        cursor.execute(customer_query, (customer_id,))

        customer = cursor.fetchone()

        if not customer:
            print("\nCustomer not found.")
            return

        customer_name = customer[0]

        # Get purchase history using customer name
        sales_query = """
        SELECT sale_id, plant_name, quantity,
            total_amount, sale_date
        FROM sales
        WHERE customer_name = %s
        """

        cursor.execute(sales_query, (customer_name,))

        sales = cursor.fetchall()

        if not sales:
            print("\nNo purchase history found.")
            return

        print("\n--------- CUSTOMER PURCHASE HISTORY ---------")

        print(f"Customer ID   : {customer_id}")
        print(f"Customer Name : {customer_name}")

        print("\nSales:")

        for sale in sales:
            print(f"""
Sale ID       : {sale[0]}
Plant Name    : {sale[1]}
Quantity      : {sale[2]}
Total Amount  : {sale[3]}
Sale Date     : {sale[4]}
----------------------------------------------
""")

    except ValueError:
        print("\nPlease enter a valid Customer ID.")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# -----------------------------------------
# CUSTOMER MENU
# -----------------------------------------
def customer_menu():

    while True:

        print("\n================================")
        print("       CUSTOMER MODULE")
        print("================================")

        print("1. Add Customer")
        print("2. View Customers")
        print("3. Customer Purchase History")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            customer_purchase_history()

        elif choice == "4":
            break

        else:
            print("\nInvalid choice. Please try again.")


# -----------------------------------------
# RUN CUSTOMER MODULE
# -----------------------------------------
if __name__ == "__main__":
    customer_menu()
