from plant_module import plant_menu
from supplier_module import supplier_menu
from customer_module import customer_menu
from billing_module import billing_menu
from reports_module import reports_menu


def main_menu():

    while True:

        print("\n========================================")
        print("       GREEN BLOOM PLANTS")
        print("    INVENTORY MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Plant Module")
        print("2. Supplier Module")
        print("3. Customer Module")
        print("4. Billing Module")
        print("5. Reports Module")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            plant_menu()

        elif choice == "2":
            supplier_menu()

        elif choice == "3":
            customer_menu()

        elif choice == "4":
            billing_menu()

        elif choice == "5":
            reports_menu()

        elif choice == "6":
            print("\nThank you for using Green Bloom Plants!")
            print("Application closed.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()