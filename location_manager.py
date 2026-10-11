from config import LOCATION_FILE, PRODUCT_FILE
from storage import load_data, save_data
from utils import generate_id, read_nonempty, find_by_id


def add_location():
    locations = load_data(LOCATION_FILE)

    code = read_nonempty("Location Code (e.g. A-01): ")

    if code is None:
        return

    code = code.upper()

    if any(location["code"] == code for location in locations):
        print("Location code already exists.")
        return

    description = input("Description: ").strip()

    location = {
        "id": generate_id("LOC"),
        "code": code,
        "description": description,
        "active": True
    }

    locations.append(location)
    save_data(LOCATION_FILE, locations)

    print("Location created successfully!")
    print("Location ID:", location["id"])


def view_locations():
    locations = load_data(LOCATION_FILE)
    products = load_data(PRODUCT_FILE)

    if not locations:
        print("No storage locations found.")
        return

    print("\n========== WAREHOUSE LOCATIONS ==========")

    for location in locations:
        count = sum(
            1 for product in products
            if product["location_id"] == location["id"]
            and product["quantity"] > 0
        )

        print("-" * 40)
        print("Location ID:", location["id"])
        print("Code:", location["code"])
        print("Description:", location["description"])
        print("Products with stock:", count)
        print("Active:", location["active"])


def assign_product_location():
    products = load_data(PRODUCT_FILE)
    locations = load_data(LOCATION_FILE)

    product_id = input("Product ID: ").strip()
    location_id = input("Location ID: ").strip()

    product = find_by_id(products, product_id)
    location = find_by_id(locations, location_id)

    if not product:
        print("Product not found.")
        return

    if not location or not location["active"]:
        print("Active storage location not found.")
        return

    product["location_id"] = location_id

    save_data(PRODUCT_FILE, products)

    print(
        f"Product {product['sku']} assigned to "
        f"location {location['code']}."
    )


def assign_product_supplier():
    products = load_data(PRODUCT_FILE)
    suppliers = load_data("data/suppliers.json")

    product_id = input("Product ID: ").strip()
    supplier_id = input("Supplier ID: ").strip()

    product = find_by_id(products, product_id)
    supplier = find_by_id(suppliers, supplier_id)

    if not product:
        print("Product not found.")
        return

    if not supplier or not supplier["active"]:
        print("Active supplier not found.")
        return

    product["supplier_id"] = supplier_id

    save_data(PRODUCT_FILE, products)

    print("Supplier assigned successfully.")
