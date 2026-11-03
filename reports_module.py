from db_connection import get_connection


# TOTAL SALES
def total_sales():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT SUM(total_amount)
        FROM sales
        """

        cursor.execute(query)

        result = cursor.fetchone()

        total = result[0]

        if total is None:
            total = 0

        print("\n================================")
        print("          TOTAL SALES")
        print("================================")
        print("Total Sales Amount :", total)

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# AVAILABLE STOCK
def available_stock():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT plant_id, plant_name, category,
               price, quantity
        FROM plants
        ORDER BY plant_id
        """

        cursor.execute(query)

        plants = cursor.fetchall()

        if not plants:
            print("\nNo plants available.")
            return

        print("\n================================")
        print("        AVAILABLE STOCK")
        print("================================")

        for plant in plants:
            print(f"""
Plant ID   : {plant[0]}
Plant Name : {plant[1]}
Category   : {plant[2]}
Price      : {plant[3]}
Quantity   : {plant[4]}
--------------------------------
""")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# LOW STOCK PLANTS
def low_stock_plants():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT plant_id, plant_name, category,
               quantity
        FROM plants
        WHERE quantity <= 5
        ORDER BY quantity
        """

        cursor.execute(query)

        plants = cursor.fetchall()

        if not plants:
            print("\nNo low-stock plants found.")
            return

        print("\n================================")
        print("        LOW STOCK PLANTS")
        print("================================")

        for plant in plants:
            print(f"""
Plant ID   : {plant[0]}
Plant Name : {plant[1]}
Category   : {plant[2]}
Quantity   : {plant[3]}
--------------------------------
""")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# CUSTOMER PURCHASE HISTORY
def customer_purchase_history():
    connection = get_connection()

    if connection is None:
        return

    try:
        customer_id = int(input("Enter Customer ID: "))

        cursor = connection.cursor()

        # Get customer name
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

        # Get purchase history
        sales_query = """
        SELECT sale_id,
               plant_name,
               quantity,
               total_amount,
               sale_date
        FROM sales
        WHERE customer_name = %s
        ORDER BY sale_id
        """

        cursor.execute(sales_query, (customer_name,))

        sales = cursor.fetchall()

        if not sales:
            print("\nNo purchase history found.")
            return

        print("\n================================")
        print("     CUSTOMER PURCHASE HISTORY")
        print("================================")

        print("Customer ID   :", customer_id)
        print("Customer Name :", customer_name)

        for sale in sales:
            print(f"""
Sale ID      : {sale[0]}
Plant Name   : {sale[1]}
Quantity     : {sale[2]}
Total Amount : {sale[3]}
Sale Date    : {sale[4]}
--------------------------------
""")

    except ValueError:
        print("\nPlease enter a valid Customer ID.")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# REPORTS MENU
def reports_menu():

    while True:

        print("\n================================")
        print("        REPORTS MODULE")
        print("================================")

        print("1. Total Sales")
        print("2. Available Stock")
        print("3. Low Stock Plants")
        print("4. Customer Purchase History")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            total_sales()

        elif choice == "2":
            available_stock()

        elif choice == "3":
            low_stock_plants()

        elif choice == "4":
            customer_purchase_history()

        elif choice == "5":
            break

        else:
            print("\nInvalid choice. Please try again.")


# RUN REPORTS MODULE
if __name__ == "__main__":
    reports_menu()