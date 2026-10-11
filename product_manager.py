from config import PRODUCT_FILE, LOW_STOCK_DEFAULT
from storage import load_data, save_data
from utils import (
    generate_id,
    find_by_id,
    read_nonempty,
    read_positive_number,
    money
)


def add_product():
    products = load_data(PRODUCT_FILE)

    name = read_nonempty("Product Name: ")
    sku = read_nonempty("SKU Code: ")

    if name is None or sku is None:
        return

    sku = sku.upper()

    if any(product["sku"] == sku for product in products):
        print("SKU already exists.")
        return

    price = read_positive_number("Unit Cost: ₹")

    if price is None:
        return

    minimum = read_positive_number(
        f"Minimum Stock Level [{LOW_STOCK_DEFAULT}]: ",
        allow_zero=True
    )

    if minimum is None:
        return

    product = {
        "id": generate_id("PRD"),
        "name": name,
        "sku": sku,
        "unit_cost": round(price, 2),
        "quantity": 0,
        "minimum_stock": int(minimum),
        "location_id": None,
        "supplier_id": None,
        "active": True
    }

    products.append(product)
    save_data(PRODUCT_FILE, products)

    print("Product created successfully!")
    print("Product ID:", product["id"])


def view_products():
    products = load_data(PRODUCT_FILE)

    if not products:
        print("No products found.")
        return

    print("\n========== PRODUCTS ==========")

    for product in products:
        print("-" * 45)
        print("Product ID:", product["id"])
        print("Name:", product["name"])
        print("SKU:", product["sku"])
        print("Unit Cost:", money(product["unit_cost"]))
        print("Quantity:", product["quantity"])
        print("Minimum Stock:", product["minimum_stock"])
        print("Location:", product["location_id"] or "Unassigned")
        print("Active:", product["active"])


def search_product():
    products = load_data(PRODUCT_FILE)

    keyword = input("Enter product name or SKU: ").strip().casefold()

    if not keyword:
        print("Enter a search term.")
        return

    results = [
        product for product in products
        if keyword in product["name"].casefold()
        or keyword in product["sku"].casefold()
    ]

    if not results:
        print("No matching products found.")
        return

    for product in results:
        print(
            product["id"],
            product["name"],
            product["sku"],
            "Quantity:", product["quantity"]
        )


def update_product():
    products = load_data(PRODUCT_FILE)

    product_id = input("Product ID: ").strip()
    product = find_by_id(products, product_id)

    if not product:
        print("Product not found.")
        return

    name = input(
        f"Name [{product['name']}], Enter to skip: "
    ).strip()

    if name:
        product["name"] = name

    cost_text = input(
        f"Unit Cost [{product['unit_cost']}], Enter to skip: "
    ).strip()

    if cost_text:
        try:
            cost = float(cost_text)

            if cost < 0:
                print("Cost cannot be negative.")
                return

            product["unit_cost"] = round(cost, 2)

        except ValueError:
            print("Invalid cost.")
            return

    minimum_text = input(
        f"Minimum Stock [{product['minimum_stock']}], Enter to skip: "
    ).strip()

    if minimum_text:
        try:
            minimum = int(minimum_text)

            if minimum < 0:
                print("Minimum stock cannot be negative.")
                return

            product["minimum_stock"] = minimum

        except ValueError:
            print("Invalid stock level.")
            return

    save_data(PRODUCT_FILE, products)
    print("Product updated successfully!")


def deactivate_product():
    products = load_data(PRODUCT_FILE)

    product_id = input("Product ID: ").strip()
    product = find_by_id(products, product_id)

    if not product:
        print("Product not found.")
        return

    if product["quantity"] > 0:
        print("Remove or transfer its stock before deactivation.")
        return

    product["active"] = False
    save_data(PRODUCT_FILE, products)

    print("Product deactivated.")
