from db_connection import get_connection
from datetime import date


# CREATE BILL
def create_bill():
    connection = get_connection()

    if connection is None:
        return

    try:
        customer_id = int(input("Enter Customer ID: "))

        cursor = connection.cursor()

        # Check customer
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

        # Get plant
        plant_id = int(input("Enter Plant ID: "))

        plant_query = """
        SELECT plant_name, price, quantity
        FROM plants
        WHERE plant_id = %s
        """

        cursor.execute(plant_query, (plant_id,))
        plant = cursor.fetchone()

        if not plant:
            print("\nPlant not found.")
            return

        plant_name = plant[0]
        price = plant[1]
        available_quantity = plant[2]

        print("\n--------- PLANT DETAILS ---------")
        print("Plant Name :", plant_name)
        print("Price      :", price)
        print("Available  :", available_quantity)

        # Enter quantity
        quantity = int(input("\nEnter Quantity: "))

        if quantity <= 0:
            print("\nQuantity must be greater than zero.")
            return

        # Check stock
        if quantity > available_quantity:
            print("\nInsufficient stock.")
            print("Available stock:", available_quantity)
            return

        # Calculate total
        total_amount = price * quantity

        # Display bill
        print("\n================================")
        print("          GREEN BLOOM")
        print("          PLANT BILL")
        print("================================")
        print("Customer ID  :", customer_id)
        print("Customer Name:", customer_name)
        print("Plant Name   :", plant_name)
        print("Price        :", price)
        print("Quantity     :", quantity)
        print("--------------------------------")
        print("Total Amount :", total_amount)
        print("Date         :", date.today())
        print("================================")

        # Insert sale
        sale_query = """
        INSERT INTO sales
        (customer_name, plant_name, quantity, total_amount, sale_date)
        VALUES (%s, %s, %s, %s, %s)
        """

        sale_values = (
            customer_name,
            plant_name,
            quantity,
            total_amount,
            date.today()
        )

        cursor.execute(sale_query, sale_values)

        # Reduce stock
        new_quantity = available_quantity - quantity

        stock_query = """
        UPDATE plants
        SET quantity = %s
        WHERE plant_id = %s
        """

        cursor.execute(stock_query, (new_quantity, plant_id))

        # Save changes
        connection.commit()

        print("\nBill generated successfully!")
        print("Remaining stock:", new_quantity)

    except ValueError:
        print("\nPlease enter valid numeric values.")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# VIEW SALES
def view_sales():
    connection = get_connection()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
        SELECT sale_id,
               customer_name,
               plant_name,
               quantity,
               total_amount,
               sale_date
        FROM sales
        ORDER BY sale_id
        """

        cursor.execute(query)

        sales = cursor.fetchall()

        if not sales:
            print("\nNo sales found.")
            return

        print("\n--------------- SALES HISTORY ---------------")

        for sale in sales:
            print(f"""
Sale ID       : {sale[0]}
Customer Name : {sale[1]}
Plant Name    : {sale[2]}
Quantity      : {sale[3]}
Total Amount  : {sale[4]}
Sale Date     : {sale[5]}
-----------------------------------------------
""")

    except Exception as error:
        print("\nError:", error)

    finally:
        connection.close()


# BILLING MENU
def billing_menu():

    while True:

        print("\n================================")
        print("        BILLING MODULE")
        print("================================")

        print("1. Create Bill")
        print("2. View Sales")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_bill()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please try again.")


# RUN BILLING MODULE
if __name__ == "__main__":
    billing_menu()