from product_manager import (
    add_product,
    view_products,
    search_product,
    update_product,
    deactivate_product
)

from supplier_manager import (
    add_supplier,
    view_suppliers,
    search_supplier
)

from location_manager import (
    add_location,
    view_locations,
    assign_product_location,
    assign_product_supplier
)

from stock_manager import (
    stock_in,
    stock_out
)

from movement_manager import (
    view_movements,
    search_movement
)

from report_manager import (
    inventory_valuation_report,
    low_stock_report,
    location_stock_report
)

from slot_manager import *  # Not required in this project.


def main():
    actions = {
        "1": add_product,
        "2": view_products,
        "3": search_product,
        "4": update_product,
        "5": deactivate_product,
        "6": add_supplier,
        "7": view_suppliers,
        "8": search_supplier,
        "9": add_location,
        "10": view_locations,
        "11": assign_product_location,
        "12": assign_product_supplier,
        "13": stock_in,
        "14": stock_out,
        "15": view_movements,
        "16": search_movement,
        "17": inventory_valuation_report,
        "18": low_stock_report,
        "19": location_stock_report
    }

    while True:
        print("\n" + "=" * 48)
        print("       WAREHOUSE MANAGEMENT SYSTEM")
        print("=" * 48)

        options = [
            "Add Product",
            "View Products",
            "Search Product",
            "Update Product",
            "Deactivate Product",
            "Add Supplier",
            "View Suppliers",
            "Search Supplier",
            "Add Warehouse Location",
            "View Warehouse Locations",
            "Assign Product Location",
            "Assign Product Supplier",
            "Record Stock In",
            "Record Stock Out",
            "View Stock Movement History",
            "Search Stock Movement",
            "Inventory Valuation Report",
            "Low Stock Report",
            "Location Stock Report"
        ]

        for number, option in enumerate(options, 1):
            print(f"{number}. {option}")

        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Warehouse Management System!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (RuntimeError, OSError) as error:
                print("Application error:", error)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
