from config import (
    PRODUCT_FILE,
    SUPPLIER_FILE,
    LOCATION_FILE
)
from storage import load_data, save_data
from utils import find_by_id, read_positive_number, current_datetime, generate_id


def record_stock_movement(direction):
    products = load_data(PRODUCT_FILE)
    suppliers = load_data(SUPPLIER_FILE)
    locations = load_data(LOCATION_FILE)

    product_id = input("Product ID: ").strip()
    product = find_by_id(products, product_id)

    if not product or not product["active"]:
        print("Active product not found.")
        return

    if not product["location_id"]:
        print("Assign a storage location before moving stock.")
        return

    location = find_by_id(
        locations,
        product["location_id"]
    )

    if not location or not location["active"]:
        print("The product's storage location is inactive or missing.")
        return

    quantity = read_positive_number("Quantity: ")

    if quantity is None or not quantity.is_integer():
        print("Quantity must be a positive whole number.")
        return

    quantity = int(quantity)

    if direction == "OUT" and quantity > product["quantity"]:
        print("Insufficient stock.")
        print("Available quantity:", product["quantity"])
        return

    supplier_id = None

    if direction == "IN":
        supplier_id = input(
            "Supplier ID (press Enter if not applicable): "
        ).strip() or None

        if supplier_id:
            supplier = find_by_id(suppliers, supplier_id)

            if not supplier or not supplier["active"]:
                print("Active supplier not found.")
                return

    # Save a movement record and update stock.
    from config import MOVEMENT_FILE

    movements = load_data(MOVEMENT_FILE)

    movement = {
        "id": generate_id("MOV"),
        "product_id": product_id,
        "sku": product["sku"],
        "direction": direction,
        "quantity": quantity,
        "supplier_id": supplier_id,
        "location_id": product["location_id"],
        "timestamp": current_datetime()
    }

    old_quantity = product["quantity"]

    if direction == "IN":
        product["quantity"] += quantity
    else:
        product["quantity"] -= quantity

    try:
        # Write the movement first, then update product stock.
        movements.append(movement)
        save_data(MOVEMENT_FILE, movements)

        save_data(PRODUCT_FILE, products)

    except RuntimeError as error:
        print("Could not save stock movement:", error)
        print(
            "Check both JSON files before retrying to avoid "
            "duplicate stock transactions."
        )
        return

    print("\nStock movement recorded successfully!")
    print("Movement ID:", movement["id"])
    print("Product:", product["name"])
    print("Previous Stock:", old_quantity)
    print("Quantity Moved:", quantity)
    print("Current Stock:", product["quantity"])


def stock_in():
    record_stock_movement("IN")


def stock_out():
    record_stock_movement("OUT")
