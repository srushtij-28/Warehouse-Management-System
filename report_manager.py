from config import PRODUCT_FILE, LOCATION_FILE
from storage import load_data
from utils import money


def inventory_valuation_report():
    products = load_data(PRODUCT_FILE)

    active_products = [
        product for product in products
        if product["active"]
    ]

    total_units = sum(
        product["quantity"]
        for product in active_products
    )

    total_value = sum(
        product["quantity"] * product["unit_cost"]
        for product in active_products
    )

    print("\n========== INVENTORY VALUATION ==========")
    print("Active Products:", len(active_products))
    print("Total Units in Stock:", total_units)
    print("Total Inventory Value:", money(total_value))
    print("=" * 40)


def low_stock_report():
    products = load_data(PRODUCT_FILE)

    low_stock = [
        product for product in products
        if product["active"]
        and product["quantity"] <= product["minimum_stock"]
    ]

    print("\n========== LOW STOCK REPORT ==========")

    if not low_stock:
        print("No low-stock products.")
        return

    for product in low_stock:
        print("-" * 40)
        print("Name:", product["name"])
        print("SKU:", product["sku"])
        print("Current Stock:", product["quantity"])
        print("Minimum Stock:", product["minimum_stock"])


def location_stock_report():
    products = load_data(PRODUCT_FILE)
    locations = load_data(LOCATION_FILE)

    print("\n========== LOCATION STOCK REPORT ==========")

    for location in locations:
        if not location["active"]:
            continue

        matching = [
            product for product in products
            if product["location_id"] == location["id"]
            and product["active"]
        ]

        quantity = sum(
            product["quantity"] for product in matching
        )

        value = sum(
            product["quantity"] * product["unit_cost"]
            for product in matching
        )

        print("-" * 40)
        print("Location:", location["code"])
        print("Products:", len(matching))
        print("Total Units:", quantity)
        print("Stock Value:", money(value))
