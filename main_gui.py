import tkinter as tk
from tkinter import messagebox


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Green Bloom Plants")
root.geometry("900x600")
root.configure(bg="#f4f7f4")


# -----------------------------
# Header
# -----------------------------
header = tk.Frame(root, bg="#2e7d32", height=100)
header.pack(fill="x")

title = tk.Label(
    header,
    text="GREEN BLOOM PLANTS",
    font=("Arial", 26, "bold"),
    bg="#2e7d32",
    fg="white"
)
title.pack(pady=(18, 2))

subtitle = tk.Label(
    header,
    text="Inventory Management System",
    font=("Arial", 13),
    bg="#2e7d32",
    fg="white"
)
subtitle.pack()


# -----------------------------
# Welcome Text
# -----------------------------
welcome = tk.Label(
    root,
    text="Welcome to Green Bloom Plants",
    font=("Arial", 20, "bold"),
    bg="#f4f7f4",
    fg="#333333"
)
welcome.pack(pady=30)


# -----------------------------
# Button Functions
# -----------------------------
def open_plants():
    plant_window = tk.Toplevel(root)
    plant_window.title("Plant Management")
    plant_window.geometry("1000x700")
    plant_window.configure(bg="#f4f7f4")

    # Title
    title = tk.Label(
        plant_window,
        text="Plant Management",
        font=("Arial", 22, "bold"),
        bg="#f4f7f4",
        fg="#2e7d32"
    )
    title.pack(pady=15)

    # Form frame
    form_frame = tk.Frame(
        plant_window,
        bg="#f4f7f4"
    )
    form_frame.pack(pady=10)

    # Plant ID
    tk.Label(
        form_frame,
        text="Plant ID:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=0, column=0, padx=10, pady=8)

    plant_id_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    plant_id_entry.grid(row=0, column=1, padx=10, pady=8)

    # Plant Name
    tk.Label(
        form_frame,
        text="Plant Name:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=1, column=0, padx=10, pady=8)

    plant_name_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    plant_name_entry.grid(row=1, column=1, padx=10, pady=8)

    # Category
    tk.Label(
        form_frame,
        text="Category:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=2, column=0, padx=10, pady=8)

    category_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    category_entry.grid(row=2, column=1, padx=10, pady=8)

    # Price
    tk.Label(
        form_frame,
        text="Price:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=3, column=0, padx=10, pady=8)

    price_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    price_entry.grid(row=3, column=1, padx=10, pady=8)

    # Quantity
    tk.Label(
        form_frame,
        text="Quantity:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=4, column=0, padx=10, pady=8)

    quantity_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    quantity_entry.grid(row=4, column=1, padx=10, pady=8)

    # Supplier
    tk.Label(
        form_frame,
        text="Supplier Name:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=5, column=0, padx=10, pady=8)

    supplier_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    supplier_entry.grid(row=5, column=1, padx=10, pady=8)

    # Add Plant Function
    def add_plant_gui():

        plant_id = plant_id_entry.get().strip()
        plant_name = plant_name_entry.get().strip()
        category = category_entry.get().strip()
        price = price_entry.get().strip()
        quantity = quantity_entry.get().strip()
        supplier_name = supplier_entry.get().strip()

        # Check empty fields
        if not plant_id or not plant_name or not category or not price or not quantity or not supplier_name:
            messagebox.showwarning(
                "Input Error",
                "Please fill all fields."
            )
            return

        try:
            plant_id = int(plant_id)
            price = float(price)
            quantity = int(quantity)

            from db_connection import get_connection

            connection = get_connection()

            if connection:
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

                cursor.close()
                connection.close()

                messagebox.showinfo(
                    "Success",
                    "Plant added successfully!"
                )

                # Clear fields
                plant_id_entry.delete(0, tk.END)
                plant_name_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
                supplier_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Plant ID and quantity must be integers.\n"
                "Price must be a number."
            )

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # Add button
    add_button = tk.Button(
        plant_window,
        text="Add Plant",
        width=20,
        height=2,
        font=("Arial", 12, "bold"),
        command=add_plant_gui
    )
    add_button.pack(pady=15)


def open_suppliers():
    supplier_window = tk.Toplevel(root)
    supplier_window.title("Supplier Management")
    supplier_window.geometry("1000x700")
    supplier_window.configure(bg="#f4f7f4")

    # -----------------------------
    # Title
    # -----------------------------
    title = tk.Label(
        supplier_window,
        text="Supplier Management",
        font=("Arial", 22, "bold"),
        bg="#f4f7f4",
        fg="#2e7d32"
    )
    title.pack(pady=15)

    # -----------------------------
    # Form Frame
    # -----------------------------
    form_frame = tk.Frame(
        supplier_window,
        bg="#f4f7f4"
    )
    form_frame.pack(pady=10)

    # -----------------------------
    # Supplier ID
    # -----------------------------
    tk.Label(
        form_frame,
        text="Supplier ID:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=0, column=0, padx=10, pady=8)

    supplier_id_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    supplier_id_entry.grid(row=0, column=1, padx=10, pady=8)

    # -----------------------------
    # Supplier Name
    # -----------------------------
    tk.Label(
        form_frame,
        text="Supplier Name:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=1, column=0, padx=10, pady=8)

    supplier_name_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    supplier_name_entry.grid(row=1, column=1, padx=10, pady=8)

    # -----------------------------
    # Phone
    # -----------------------------
    tk.Label(
        form_frame,
        text="Phone:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=2, column=0, padx=10, pady=8)

    phone_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    phone_entry.grid(row=2, column=1, padx=10, pady=8)

    # -----------------------------
    # City
    # -----------------------------
    tk.Label(
        form_frame,
        text="City:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=3, column=0, padx=10, pady=8)

    city_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    city_entry.grid(row=3, column=1, padx=10, pady=8)

    # -----------------------------
    # Add Supplier
    # -----------------------------
    def add_supplier_gui():

        supplier_id = supplier_id_entry.get().strip()
        supplier_name = supplier_name_entry.get().strip()
        phone = phone_entry.get().strip()
        city = city_entry.get().strip()

        if not supplier_id or not supplier_name or not phone or not city:
            messagebox.showwarning(
                "Input Error",
                "Please fill all fields."
            )
            return

        try:
            from db_connection import get_connection

            connection = get_connection()

            if connection:

                cursor = connection.cursor()

                query = """
                INSERT INTO suppliers
                (supplier_id, supplier_name, phone, city)
                VALUES (%s, %s, %s, %s)
                """

                values = (
                    supplier_id,
                    supplier_name,
                    phone,
                    city
                )

                cursor.execute(query, values)
                connection.commit()

                cursor.close()
                connection.close()

                messagebox.showinfo(
                    "Success",
                    "Supplier added successfully!"
                )

                supplier_id_entry.delete(0, tk.END)
                supplier_name_entry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)
                city_entry.delete(0, tk.END)

            else:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # View Suppliers
    # -----------------------------
    def view_suppliers_gui():

        view_window = tk.Toplevel(supplier_window)
        view_window.title("View Suppliers")
        view_window.geometry("800x500")
        view_window.configure(bg="#f4f7f4")

        title = tk.Label(
            view_window,
            text="Supplier List",
            font=("Arial", 20, "bold"),
            bg="#f4f7f4",
            fg="#2e7d32"
        )
        title.pack(pady=15)

        from tkinter import ttk
        from db_connection import get_connection

        columns = (
            "supplier_id",
            "supplier_name",
            "phone",
            "city"
        )

        tree = ttk.Treeview(
            view_window,
            columns=columns,
            show="headings"
        )

        tree.heading(
            "supplier_id",
            text="Supplier ID"
        )

        tree.heading(
            "supplier_name",
            text="Supplier Name"
        )

        tree.heading(
            "phone",
            text="Phone"
        )

        tree.heading(
            "city",
            text="City"
        )

        tree.column(
            "supplier_id",
            width=120
        )

        tree.column(
            "supplier_name",
            width=200
        )

        tree.column(
            "phone",
            width=150
        )

        tree.column(
            "city",
            width=150
        )

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        try:

            connection = get_connection()

            if connection:

                cursor = connection.cursor()

                query = """
                SELECT
                    supplier_id,
                    supplier_name,
                    phone,
                    city
                FROM suppliers
                """

                cursor.execute(query)

                rows = cursor.fetchall()

                for row in rows:
                    tree.insert(
                        "",
                        tk.END,
                        values=row
                    )

                cursor.close()
                connection.close()

            else:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # Update Supplier
    # -----------------------------
    def update_supplier_gui():

        supplier_id = supplier_id_entry.get().strip()
        supplier_name = supplier_name_entry.get().strip()
        phone = phone_entry.get().strip()
        city = city_entry.get().strip()

        if not supplier_id:
            messagebox.showwarning(
                "Input Error",
                "Enter Supplier ID to update."
            )
            return

        if not supplier_name or not phone or not city:
            messagebox.showwarning(
                "Input Error",
                "Please fill all fields."
            )
            return

        try:

            from db_connection import get_connection

            connection = get_connection()

            if connection:

                cursor = connection.cursor()

                query = """
                UPDATE suppliers
                SET supplier_name = %s,
                    phone = %s,
                    city = %s
                WHERE supplier_id = %s
                """

                values = (
                    supplier_name,
                    phone,
                    city,
                    supplier_id
                )

                cursor.execute(query, values)
                connection.commit()

                if cursor.rowcount > 0:

                    messagebox.showinfo(
                        "Success",
                        "Supplier updated successfully!"
                    )

                else:

                    messagebox.showwarning(
                        "Not Found",
                        "Supplier ID not found."
                    )

                cursor.close()
                connection.close()

            else:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # Delete Supplier
    # -----------------------------
    def delete_supplier_gui():

        supplier_id = supplier_id_entry.get().strip()

        if not supplier_id:
            messagebox.showwarning(
                "Input Error",
                "Enter Supplier ID to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this supplier?"
        )

        if not confirm:
            return

        try:

            from db_connection import get_connection

            connection = get_connection()

            if connection:

                cursor = connection.cursor()

                query = """
                DELETE FROM suppliers
                WHERE supplier_id = %s
                """

                cursor.execute(
                    query,
                    (supplier_id,)
                )

                connection.commit()

                if cursor.rowcount > 0:

                    messagebox.showinfo(
                        "Success",
                        "Supplier deleted successfully!"
                    )

                    supplier_id_entry.delete(0, tk.END)
                    supplier_name_entry.delete(0, tk.END)
                    phone_entry.delete(0, tk.END)
                    city_entry.delete(0, tk.END)

                else:

                    messagebox.showwarning(
                        "Not Found",
                        "Supplier ID not found."
                    )

                cursor.close()
                connection.close()

            else:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # Buttons Frame
    # -----------------------------
    button_frame = tk.Frame(
        supplier_window,
        bg="#f4f7f4"
    )
    button_frame.pack(pady=20)

    # Add Button
    add_button = tk.Button(
        button_frame,
        text="Add Supplier",
        width=18,
        height=2,
        font=("Arial", 11, "bold"),
        command=add_supplier_gui
    )
    add_button.grid(
        row=0,
        column=0,
        padx=8,
        pady=8
    )

    # View Button
    view_button = tk.Button(
        button_frame,
        text="View Suppliers",
        width=18,
        height=2,
        font=("Arial", 11, "bold"),
        command=view_suppliers_gui
    )
    view_button.grid(
        row=0,
        column=1,
        padx=8,
        pady=8
    )

    # Update Button
    update_button = tk.Button(
        button_frame,
        text="Update Supplier",
        width=18,
        height=2,
        font=("Arial", 11, "bold"),
        command=update_supplier_gui
    )
    update_button.grid(
        row=1,
        column=0,
        padx=8,
        pady=8
    )

    # Delete Button
    delete_button = tk.Button(
        button_frame,
        text="Delete Supplier",
        width=18,
        height=2,
        font=("Arial", 11, "bold"),
        command=delete_supplier_gui
    )
    delete_button.grid(
        row=1,
        column=1,
        padx=8,
        pady=8
    )

def open_customers():
    customer_window = tk.Toplevel(root)
    customer_window.title("Customer Management")
    customer_window.geometry("1000x700")
    customer_window.configure(bg="#f4f7f4")

    # -----------------------------
    # Title
    # -----------------------------
    title = tk.Label(
        customer_window,
        text="Customer Management",
        font=("Arial", 22, "bold"),
        bg="#f4f7f4",
        fg="#2e7d32"
    )
    title.pack(pady=15)

    # -----------------------------
    # Form Frame
    # -----------------------------
    form_frame = tk.Frame(
        customer_window,
        bg="#f4f7f4"
    )
    form_frame.pack(pady=10)

    # -----------------------------
    # Customer ID
    # -----------------------------
    tk.Label(
        form_frame,
        text="Customer ID:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=0, column=0, padx=10, pady=8)

    customer_id_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    customer_id_entry.grid(row=0, column=1, padx=10, pady=8)

    # -----------------------------
    # Customer Name
    # -----------------------------
    tk.Label(
        form_frame,
        text="Customer Name:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=1, column=0, padx=10, pady=8)

    customer_name_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    customer_name_entry.grid(row=1, column=1, padx=10, pady=8)

    # -----------------------------
    # Phone
    # -----------------------------
    tk.Label(
        form_frame,
        text="Phone:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=2, column=0, padx=10, pady=8)

    phone_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    phone_entry.grid(row=2, column=1, padx=10, pady=8)

    # -----------------------------
    # City
    # -----------------------------
    tk.Label(
        form_frame,
        text="City:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=3, column=0, padx=10, pady=8)

    city_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    city_entry.grid(row=3, column=1, padx=10, pady=8)

    # -----------------------------
    # Add Customer
    # -----------------------------
    def add_customer_gui():

        customer_id = customer_id_entry.get().strip()
        customer_name = customer_name_entry.get().strip()
        phone = phone_entry.get().strip()
        city = city_entry.get().strip()

        if not customer_id or not customer_name or not phone or not city:
            messagebox.showwarning(
                "Input Error",
                "Please fill all fields."
            )
            return

        try:
            customer_id = int(customer_id)

            from db_connection import get_connection

            connection = get_connection()

            if connection:

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

                cursor.close()
                connection.close()

                messagebox.showinfo(
                    "Success",
                    "Customer added successfully!"
                )

                # Clear fields
                customer_id_entry.delete(0, tk.END)
                customer_name_entry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)
                city_entry.delete(0, tk.END)

            else:

                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Customer ID must be an integer."
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # View Customers
    # -----------------------------
    def view_customers_gui():

        view_window = tk.Toplevel(customer_window)
        view_window.title("View Customers")
        view_window.geometry("800x500")
        view_window.configure(bg="#f4f7f4")

        title = tk.Label(
            view_window,
            text="Customer List",
            font=("Arial", 20, "bold"),
            bg="#f4f7f4",
            fg="#2e7d32"
        )
        title.pack(pady=15)

        from tkinter import ttk
        from db_connection import get_connection

        # Table columns
        columns = (
            "customer_id",
            "customer_name",
            "phone",
            "city"
        )

        tree = ttk.Treeview(
            view_window,
            columns=columns,
            show="headings"
        )

        # Headings
        tree.heading(
            "customer_id",
            text="Customer ID"
        )

        tree.heading(
            "customer_name",
            text="Customer Name"
        )

        tree.heading(
            "phone",
            text="Phone"
        )

        tree.heading(
            "city",
            text="City"
        )

        # Column widths
        tree.column(
            "customer_id",
            width=120
        )

        tree.column(
            "customer_name",
            width=200
        )

        tree.column(
            "phone",
            width=150
        )

        tree.column(
            "city",
            width=150
        )

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # Get customers from MySQL
        try:

            connection = get_connection()

            if connection:

                cursor = connection.cursor()

                query = """
                SELECT
                    customer_id,
                    customer_name,
                    phone,
                    city
                FROM customers
                """

                cursor.execute(query)

                rows = cursor.fetchall()

                for row in rows:

                    tree.insert(
                        "",
                        tk.END,
                        values=row
                    )

                cursor.close()
                connection.close()

            else:

                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # Purchase History
    # -----------------------------
    def purchase_history_gui():

        customer_id = customer_id_entry.get().strip()

        if not customer_id:

            messagebox.showwarning(
                "Input Error",
                "Enter Customer ID to view purchase history."
            )
            return

        try:

            customer_id = int(customer_id)

            from tkinter import ttk
            from db_connection import get_connection

            connection = get_connection()

            if connection:

                cursor = connection.cursor()

                # First get customer name
                customer_query = """
                SELECT customer_name
                FROM customers
                WHERE customer_id = %s
                """

                cursor.execute(
                    customer_query,
                    (customer_id,)
                )

                customer = cursor.fetchone()

                if not customer:

                    messagebox.showwarning(
                        "Not Found",
                        "Customer ID not found."
                    )

                    cursor.close()
                    connection.close()
                    return

                customer_name = customer[0]

                # Get purchase history
                sales_query = """
                SELECT
                    sale_id,
                    customer_name,
                    plant_name,
                    quantity,
                    total_amount,
                    sale_date
                FROM sales
                WHERE customer_name = %s
                """

                cursor.execute(
                    sales_query,
                    (customer_name,)
                )

                rows = cursor.fetchall()

                cursor.close()
                connection.close()

                # Create history window
                history_window = tk.Toplevel(customer_window)

                history_window.title(
                    "Customer Purchase History"
                )

                history_window.geometry(
                    "950x500"
                )

                history_window.configure(
                    bg="#f4f7f4"
                )

                title = tk.Label(
                    history_window,
                    text=f"Purchase History - {customer_name}",
                    font=("Arial", 20, "bold"),
                    bg="#f4f7f4",
                    fg="#2e7d32"
                )

                title.pack(pady=15)

                # Table
                columns = (
                    "sale_id",
                    "customer_name",
                    "plant_name",
                    "quantity",
                    "total_amount",
                    "sale_date"
                )

                tree = ttk.Treeview(
                    history_window,
                    columns=columns,
                    show="headings"
                )

                tree.heading(
                    "sale_id",
                    text="Sale ID"
                )

                tree.heading(
                    "customer_name",
                    text="Customer"
                )

                tree.heading(
                    "plant_name",
                    text="Plant"
                )

                tree.heading(
                    "quantity",
                    text="Quantity"
                )

                tree.heading(
                    "total_amount",
                    text="Total Amount"
                )

                tree.heading(
                    "sale_date",
                    text="Sale Date"
                )

                tree.column(
                    "sale_id",
                    width=80
                )

                tree.column(
                    "customer_name",
                    width=150
                )

                tree.column(
                    "plant_name",
                    width=150
                )

                tree.column(
                    "quantity",
                    width=100
                )

                tree.column(
                    "total_amount",
                    width=130
                )

                tree.column(
                    "sale_date",
                    width=120
                )

                tree.pack(
                    fill="both",
                    expand=True,
                    padx=20,
                    pady=10
                )

                if rows:

                    for row in rows:

                        tree.insert(
                            "",
                            tk.END,
                            values=row
                        )

                else:

                    messagebox.showinfo(
                        "Purchase History",
                        "No purchases found for this customer."
                    )

            else:

                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Customer ID must be an integer."
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # Buttons Frame
    # -----------------------------
    button_frame = tk.Frame(
        customer_window,
        bg="#f4f7f4"
    )

    button_frame.pack(pady=20)

    # Add Customer Button
    add_button = tk.Button(
        button_frame,
        text="Add Customer",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=add_customer_gui
    )

    add_button.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    # View Customers Button
    view_button = tk.Button(
        button_frame,
        text="View Customers",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=view_customers_gui
    )

    view_button.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # Purchase History Button
    history_button = tk.Button(
        button_frame,
        text="Purchase History",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=purchase_history_gui
    )

    history_button.grid(
        row=1,
        column=0,
        columnspan=2,
        padx=10,
        pady=10
    )


def open_billing():
    billing_window = tk.Toplevel(root)
    billing_window.title("Billing Management")
    billing_window.geometry("1000x750")
    billing_window.configure(bg="#f4f7f4")

    # -----------------------------
    # Title
    # -----------------------------
    title = tk.Label(
        billing_window,
        text="Billing Management",
        font=("Arial", 22, "bold"),
        bg="#f4f7f4",
        fg="#2e7d32"
    )
    title.pack(pady=15)

    # -----------------------------
    # Form Frame
    # -----------------------------
    form_frame = tk.Frame(
        billing_window,
        bg="#f4f7f4"
    )
    form_frame.pack(pady=10)

    # -----------------------------
    # Customer ID
    # -----------------------------
    tk.Label(
        form_frame,
        text="Customer ID:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=0, column=0, padx=10, pady=10)

    customer_id_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    customer_id_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # -----------------------------
    # Plant ID
    # -----------------------------
    tk.Label(
        form_frame,
        text="Plant ID:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=1, column=0, padx=10, pady=10)

    plant_id_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    plant_id_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    # -----------------------------
    # Quantity
    # -----------------------------
    tk.Label(
        form_frame,
        text="Quantity:",
        font=("Arial", 12),
        bg="#f4f7f4"
    ).grid(row=2, column=0, padx=10, pady=10)

    quantity_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12)
    )
    quantity_entry.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

    # -----------------------------
    # Total Amount
    # -----------------------------
    tk.Label(
        form_frame,
        text="Total Amount:",
        font=("Arial", 12, "bold"),
        bg="#f4f7f4"
    ).grid(row=3, column=0, padx=10, pady=10)

    total_entry = tk.Entry(
        form_frame,
        width=30,
        font=("Arial", 12, "bold")
    )
    total_entry.grid(
        row=3,
        column=1,
        padx=10,
        pady=10
    )

    # -----------------------------
    # Calculate Total
    # -----------------------------
    def calculate_total():

        customer_id = customer_id_entry.get().strip()
        plant_id = plant_id_entry.get().strip()
        quantity = quantity_entry.get().strip()

        if not customer_id or not plant_id or not quantity:
            messagebox.showwarning(
                "Input Error",
                "Please enter Customer ID, Plant ID and Quantity."
            )
            return

        try:
            customer_id = int(customer_id)
            plant_id = int(plant_id)
            quantity = int(quantity)

            if quantity <= 0:
                messagebox.showwarning(
                    "Input Error",
                    "Quantity must be greater than 0."
                )
                return

            from db_connection import get_connection

            connection = get_connection()

            if not connection:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )
                return

            cursor = connection.cursor()

            # -----------------------------
            # Check Customer
            # -----------------------------
            customer_query = """
            SELECT customer_name
            FROM customers
            WHERE customer_id = %s
            """

            cursor.execute(
                customer_query,
                (customer_id,)
            )

            customer = cursor.fetchone()

            if not customer:
                messagebox.showwarning(
                    "Customer Not Found",
                    "Customer ID does not exist."
                )

                cursor.close()
                connection.close()
                return

            # -----------------------------
            # Get Plant Details
            # -----------------------------
            plant_query = """
            SELECT plant_name, price, quantity
            FROM plants
            WHERE plant_id = %s
            """

            cursor.execute(
                plant_query,
                (plant_id,)
            )

            plant = cursor.fetchone()

            if not plant:
                messagebox.showwarning(
                    "Plant Not Found",
                    "Plant ID does not exist."
                )

                cursor.close()
                connection.close()
                return

            plant_name = plant[0]
            price = float(plant[1])
            available_quantity = int(plant[2])

            # -----------------------------
            # Check Stock
            # -----------------------------
            if quantity > available_quantity:
                messagebox.showwarning(
                    "Insufficient Stock",
                    f"Only {available_quantity} plants are available."
                )

                cursor.close()
                connection.close()
                return

            # -----------------------------
            # Calculate Total
            # -----------------------------
            total_amount = price * quantity

            # -----------------------------
            # Display Total
            # -----------------------------
            total_entry.delete(0, tk.END)

            total_entry.insert(
                0,
                f"₹ {total_amount:.2f}"
            )

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Total Calculated",
                f"Plant: {plant_name}\n"
                f"Price: ₹{price:.2f}\n"
                f"Quantity: {quantity}\n"
                f"Total Amount: ₹{total_amount:.2f}"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Customer ID, Plant ID and Quantity must be integers."
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    # -----------------------------
    # Generate Bill
    # -----------------------------
    def generate_bill():

        customer_id = customer_id_entry.get().strip()
        plant_id = plant_id_entry.get().strip()
        quantity = quantity_entry.get().strip()

        if not customer_id or not plant_id or not quantity:
            messagebox.showwarning(
                "Input Error",
                "Please fill all billing fields."
            )
            return

        try:
            customer_id = int(customer_id)
            plant_id = int(plant_id)
            quantity = int(quantity)

            if quantity <= 0:
                messagebox.showwarning(
                    "Input Error",
                    "Quantity must be greater than 0."
                )
                return

            from db_connection import get_connection
            from datetime import date

            connection = get_connection()

            if not connection:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )
                return

            cursor = connection.cursor()

            # -----------------------------
            # Get Customer
            # -----------------------------
            customer_query = """
            SELECT customer_name
            FROM customers
            WHERE customer_id = %s
            """

            cursor.execute(
                customer_query,
                (customer_id,)
            )

            customer = cursor.fetchone()

            if not customer:
                messagebox.showwarning(
                    "Customer Not Found",
                    "Customer ID does not exist."
                )

                cursor.close()
                connection.close()
                return

            customer_name = customer[0]

            # -----------------------------
            # Get Plant
            # -----------------------------
            plant_query = """
            SELECT plant_name, price, quantity
            FROM plants
            WHERE plant_id = %s
            """

            cursor.execute(
                plant_query,
                (plant_id,)
            )

            plant = cursor.fetchone()

            if not plant:
                messagebox.showwarning(
                    "Plant Not Found",
                    "Plant ID does not exist."
                )

                cursor.close()
                connection.close()
                return

            plant_name = plant[0]
            price = float(plant[1])
            available_quantity = int(plant[2])

            # -----------------------------
            # Check Stock
            # -----------------------------
            if quantity > available_quantity:
                messagebox.showwarning(
                    "Insufficient Stock",
                    f"Available stock: {available_quantity}"
                )

                cursor.close()
                connection.close()
                return

            # -----------------------------
            # Calculate Total
            # -----------------------------
            total_amount = price * quantity

            # -----------------------------
            # Insert Sale
            # -----------------------------
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

            cursor.execute(
                sale_query,
                sale_values
            )

            # -----------------------------
            # Reduce Stock
            # -----------------------------
            new_quantity = available_quantity - quantity

            update_query = """
            UPDATE plants
            SET quantity = %s
            WHERE plant_id = %s
            """

            cursor.execute(
                update_query,
                (new_quantity, plant_id)
            )

            # -----------------------------
            # Save Changes
            # -----------------------------
            connection.commit()

            # -----------------------------
            # Get Sale ID
            # -----------------------------
            sale_id = cursor.lastrowid

            cursor.close()
            connection.close()

            # -----------------------------
            # Display Bill
            # -----------------------------
            bill_text = (
                "================================\n"
                "       GREEN BLOOM PLANTS\n"
                "             BILL\n"
                "================================\n\n"
                f"Sale ID       : {sale_id}\n"
                f"Customer      : {customer_name}\n"
                f"Plant         : {plant_name}\n"
                f"Price         : ₹{price:.2f}\n"
                f"Quantity      : {quantity}\n"
                f"Total Amount  : ₹{total_amount:.2f}\n"
                f"Date          : {date.today()}\n\n"
                "================================\n"
                "          Thank You!\n"
                "================================"
            )

            messagebox.showinfo(
                "Bill Generated",
                bill_text
            )

            # Clear fields
            customer_id_entry.delete(0, tk.END)
            plant_id_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            total_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Customer ID, Plant ID and Quantity must be integers."
            )

        except Exception as error:
            messagebox.showerror(
                "Billing Error",
                str(error)
            )

    # -----------------------------
    # View Sales
    # -----------------------------
    def view_sales_gui():

        sales_window = tk.Toplevel(
            billing_window
        )

        sales_window.title(
            "Sales Records"
        )

        sales_window.geometry(
            "950x500"
        )

        sales_window.configure(
            bg="#f4f7f4"
        )

        title = tk.Label(
            sales_window,
            text="Sales Records",
            font=("Arial", 20, "bold"),
            bg="#f4f7f4",
            fg="#2e7d32"
        )

        title.pack(pady=15)

        from tkinter import ttk
        from db_connection import get_connection

        columns = (
            "sale_id",
            "customer_name",
            "plant_name",
            "quantity",
            "total_amount",
            "sale_date"
        )

        tree = ttk.Treeview(
            sales_window,
            columns=columns,
            show="headings"
        )

        tree.heading(
            "sale_id",
            text="Sale ID"
        )

        tree.heading(
            "customer_name",
            text="Customer"
        )

        tree.heading(
            "plant_name",
            text="Plant"
        )

        tree.heading(
            "quantity",
            text="Quantity"
        )

        tree.heading(
            "total_amount",
            text="Total Amount"
        )

        tree.heading(
            "sale_date",
            text="Sale Date"
        )

        tree.column(
            "sale_id",
            width=80
        )

        tree.column(
            "customer_name",
            width=150
        )

        tree.column(
            "plant_name",
            width=150
        )

        tree.column(
            "quantity",
            width=100
        )

        tree.column(
            "total_amount",
            width=130
        )

        tree.column(
            "sale_date",
            width=120
        )

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        try:

            connection = get_connection()

            if connection:

                cursor = connection.cursor()

                query = """
                SELECT
                    sale_id,
                    customer_name,
                    plant_name,
                    quantity,
                    total_amount,
                    sale_date
                FROM sales
                ORDER BY sale_id DESC
                """

                cursor.execute(query)

                rows = cursor.fetchall()

                for row in rows:

                    tree.insert(
                        "",
                        tk.END,
                        values=row
                    )

                cursor.close()
                connection.close()

            else:

                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # -----------------------------
    # Buttons Frame
    # -----------------------------
    button_frame = tk.Frame(
        billing_window,
        bg="#f4f7f4"
    )

    button_frame.pack(
        pady=20
    )

    # Calculate Total Button
    calculate_button = tk.Button(
        button_frame,
        text="Calculate Total",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=calculate_total
    )

    calculate_button.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    # Generate Bill Button
    bill_button = tk.Button(
        button_frame,
        text="Generate Bill",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=generate_bill
    )

    bill_button.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # View Sales Button
    sales_button = tk.Button(
        button_frame,
        text="View Sales",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=view_sales_gui
    )

    sales_button.grid(
        row=1,
        column=0,
        columnspan=2,
        padx=10,
        pady=10
    )

def open_reports():

    reports_window = tk.Toplevel(root)
    reports_window.title("Reports Management")
    reports_window.geometry("1000x700")
    reports_window.configure(bg="#f4f7f4")

    # -----------------------------
    # Title
    # -----------------------------
    title = tk.Label(
        reports_window,
        text="Reports Management",
        font=("Arial", 22, "bold"),
        bg="#f4f7f4",
        fg="#2e7d32"
    )
    title.pack(pady=15)

    # -----------------------------
    # Report Display Area
    # -----------------------------
    report_frame = tk.Frame(
        reports_window,
        bg="#f4f7f4"
    )
    report_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    # -----------------------------
    # Clear Previous Report
    # -----------------------------
    def clear_report():

        for widget in report_frame.winfo_children():
            widget.destroy()

    # -----------------------------
    # Total Sales Report
    # -----------------------------
    def total_sales_report():

        clear_report()

        from db_connection import get_connection
        from tkinter import ttk

        try:

            connection = get_connection()

            if not connection:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )
                return

            cursor = connection.cursor()

            query = """
            SELECT
                sale_id,
                customer_name,
                plant_name,
                quantity,
                total_amount,
                sale_date
            FROM sales
            ORDER BY sale_id DESC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            # Heading
            heading = tk.Label(
                report_frame,
                text="Total Sales Report",
                font=("Arial", 18, "bold"),
                bg="#f4f7f4",
                fg="#2e7d32"
            )

            heading.pack(pady=10)

            # Calculate total sales
            total_query = """
            SELECT COALESCE(SUM(total_amount), 0)
            FROM sales
            """

            cursor.execute(total_query)

            total_sales = cursor.fetchone()[0]

            total_label = tk.Label(
                report_frame,
                text=f"Total Sales Amount: ₹{float(total_sales):.2f}",
                font=("Arial", 14, "bold"),
                bg="#f4f7f4",
                fg="#333333"
            )

            total_label.pack(pady=10)

            # Table
            columns = (
                "sale_id",
                "customer_name",
                "plant_name",
                "quantity",
                "total_amount",
                "sale_date"
            )

            tree = ttk.Treeview(
                report_frame,
                columns=columns,
                show="headings"
            )

            tree.heading(
                "sale_id",
                text="Sale ID"
            )

            tree.heading(
                "customer_name",
                text="Customer"
            )

            tree.heading(
                "plant_name",
                text="Plant"
            )

            tree.heading(
                "quantity",
                text="Quantity"
            )

            tree.heading(
                "total_amount",
                text="Total Amount"
            )

            tree.heading(
                "sale_date",
                text="Sale Date"
            )

            tree.column(
                "sale_id",
                width=80
            )

            tree.column(
                "customer_name",
                width=160
            )

            tree.column(
                "plant_name",
                width=160
            )

            tree.column(
                "quantity",
                width=100
            )

            tree.column(
                "total_amount",
                width=140
            )

            tree.column(
                "sale_date",
                width=120
            )

            tree.pack(
                fill="both",
                expand=True,
                padx=10,
                pady=10
            )

            for row in rows:

                tree.insert(
                    "",
                    tk.END,
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Report Error",
                str(error)
            )

    # -----------------------------
    # Available Stock Report
    # -----------------------------
    def available_stock_report():

        clear_report()

        from db_connection import get_connection
        from tkinter import ttk

        try:

            connection = get_connection()

            if not connection:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )
                return

            cursor = connection.cursor()

            query = """
            SELECT
                plant_id,
                plant_name,
                category,
                price,
                quantity,
                supplier_name
            FROM plants
            ORDER BY plant_id
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            heading = tk.Label(
                report_frame,
                text="Available Stock Report",
                font=("Arial", 18, "bold"),
                bg="#f4f7f4",
                fg="#2e7d32"
            )

            heading.pack(pady=10)

            columns = (
                "plant_id",
                "plant_name",
                "category",
                "price",
                "quantity",
                "supplier_name"
            )

            tree = ttk.Treeview(
                report_frame,
                columns=columns,
                show="headings"
            )

            headings = {
                "plant_id": "Plant ID",
                "plant_name": "Plant Name",
                "category": "Category",
                "price": "Price",
                "quantity": "Quantity",
                "supplier_name": "Supplier"
            }

            for column in columns:

                tree.heading(
                    column,
                    text=headings[column]
                )

            tree.column(
                "plant_id",
                width=80
            )

            tree.column(
                "plant_name",
                width=160
            )

            tree.column(
                "category",
                width=130
            )

            tree.column(
                "price",
                width=100
            )

            tree.column(
                "quantity",
                width=100
            )

            tree.column(
                "supplier_name",
                width=160
            )

            tree.pack(
                fill="both",
                expand=True,
                padx=10,
                pady=10
            )

            for row in rows:

                tree.insert(
                    "",
                    tk.END,
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Report Error",
                str(error)
            )

    # -----------------------------
    # Low Stock Report
    # -----------------------------
    def low_stock_report():

        clear_report()

        from db_connection import get_connection
        from tkinter import ttk

        try:

            connection = get_connection()

            if not connection:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )
                return

            cursor = connection.cursor()

            query = """
            SELECT
                plant_id,
                plant_name,
                category,
                price,
                quantity,
                supplier_name
            FROM plants
            WHERE quantity <= 5
            ORDER BY quantity ASC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            heading = tk.Label(
                report_frame,
                text="Low Stock Plants",
                font=("Arial", 18, "bold"),
                bg="#f4f7f4",
                fg="#c62828"
            )

            heading.pack(pady=10)

            columns = (
                "plant_id",
                "plant_name",
                "category",
                "price",
                "quantity",
                "supplier_name"
            )

            tree = ttk.Treeview(
                report_frame,
                columns=columns,
                show="headings"
            )

            headings = {
                "plant_id": "Plant ID",
                "plant_name": "Plant Name",
                "category": "Category",
                "price": "Price",
                "quantity": "Quantity",
                "supplier_name": "Supplier"
            }

            for column in columns:

                tree.heading(
                    column,
                    text=headings[column]
                )

            tree.column(
                "plant_id",
                width=80
            )

            tree.column(
                "plant_name",
                width=160
            )

            tree.column(
                "category",
                width=130
            )

            tree.column(
                "price",
                width=100
            )

            tree.column(
                "quantity",
                width=100
            )

            tree.column(
                "supplier_name",
                width=160
            )

            tree.pack(
                fill="both",
                expand=True,
                padx=10,
                pady=10
            )

            for row in rows:

                tree.insert(
                    "",
                    tk.END,
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Report Error",
                str(error)
            )

    # -----------------------------
    # Customer Purchase History
    # -----------------------------
    def customer_purchase_history():

        clear_report()

        from db_connection import get_connection
        from tkinter import ttk

        try:

            connection = get_connection()

            if not connection:
                messagebox.showerror(
                    "Database Error",
                    "Could not connect to database."
                )
                return

            cursor = connection.cursor()

            query = """
            SELECT
                sale_id,
                customer_name,
                plant_name,
                quantity,
                total_amount,
                sale_date
            FROM sales
            ORDER BY customer_name, sale_date DESC
            """

            cursor.execute(query)

            rows = cursor.fetchall()

            heading = tk.Label(
                report_frame,
                text="Customer Purchase History",
                font=("Arial", 18, "bold"),
                bg="#f4f7f4",
                fg="#2e7d32"
            )

            heading.pack(pady=10)

            columns = (
                "sale_id",
                "customer_name",
                "plant_name",
                "quantity",
                "total_amount",
                "sale_date"
            )

            tree = ttk.Treeview(
                report_frame,
                columns=columns,
                show="headings"
            )

            headings = {
                "sale_id": "Sale ID",
                "customer_name": "Customer",
                "plant_name": "Plant",
                "quantity": "Quantity",
                "total_amount": "Total Amount",
                "sale_date": "Sale Date"
            }

            for column in columns:

                tree.heading(
                    column,
                    text=headings[column]
                )

            tree.column(
                "sale_id",
                width=80
            )

            tree.column(
                "customer_name",
                width=170
            )

            tree.column(
                "plant_name",
                width=170
            )

            tree.column(
                "quantity",
                width=100
            )

            tree.column(
                "total_amount",
                width=140
            )

            tree.column(
                "sale_date",
                width=120
            )

            tree.pack(
                fill="both",
                expand=True,
                padx=10,
                pady=10
            )

            for row in rows:

                tree.insert(
                    "",
                    tk.END,
                    values=row
                )

            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Report Error",
                str(error)
            )

    # -----------------------------
    # Buttons Frame
    # -----------------------------
    button_frame = tk.Frame(
        reports_window,
        bg="#f4f7f4"
    )

    button_frame.pack(
        pady=15
    )

    # Total Sales
    tk.Button(
        button_frame,
        text="Total Sales",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=total_sales_report
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    # Available Stock
    tk.Button(
        button_frame,
        text="Available Stock",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=available_stock_report
    ).grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    # Low Stock
    tk.Button(
        button_frame,
        text="Low Stock Plants",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        command=low_stock_report
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    # Customer Purchase History
    tk.Button(
        button_frame,
        text="Customer Purchase History",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        command=customer_purchase_history
    ).grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )


def exit_application():
    root.destroy()


# -----------------------------
# Button Frame
# -----------------------------
button_frame = tk.Frame(root, bg="#f4f7f4")
button_frame.pack()


# -----------------------------
# Buttons
# -----------------------------
plant_button = tk.Button(
    button_frame,
    text="🌱  Plants",
    width=20,
    height=3,
    font=("Arial", 13, "bold"),
    command=open_plants
)
plant_button.grid(row=0, column=0, padx=15, pady=15)


supplier_button = tk.Button(
    button_frame,
    text="🚚  Suppliers",
    width=20,
    height=3,
    font=("Arial", 13, "bold"),
    command=open_suppliers
)
supplier_button.grid(row=0, column=1, padx=15, pady=15)


customer_button = tk.Button(
    button_frame,
    text="👤  Customers",
    width=20,
    height=3,
    font=("Arial", 13, "bold"),
    command=open_customers
)
customer_button.grid(row=1, column=0, padx=15, pady=15)


billing_button = tk.Button(
    button_frame,
    text="🧾  Billing",
    width=20,
    height=3,
    font=("Arial", 13, "bold"),
    command=open_billing
)
billing_button.grid(row=1, column=1, padx=15, pady=15)


reports_button = tk.Button(
    button_frame,
    text="📊  Reports",
    width=20,
    height=3,
    font=("Arial", 13, "bold"),
    command=open_reports
)
reports_button.grid(row=2, column=0, padx=15, pady=15)


exit_button = tk.Button(
    button_frame,
    text="❌  Exit",
    width=20,
    height=3,
    font=("Arial", 13, "bold"),
    command=exit_application
)
exit_button.grid(row=2, column=1, padx=15, pady=15)


# -----------------------------
# Start Application
# -----------------------------
root.mainloop()