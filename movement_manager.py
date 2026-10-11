from config import MOVEMENT_FILE
from storage import load_data
from utils import find_by_id


def view_movements():
    movements = load_data(MOVEMENT_FILE)

    if not movements:
        print("No stock movements found.")
        return

    print("\n========== STOCK MOVEMENT HISTORY ==========")

    for movement in reversed(movements):
        print("-" * 45)
        print("Movement ID:", movement["id"])
        print("SKU:", movement["sku"])
        print("Direction:", movement["direction"])
        print("Quantity:", movement["quantity"])
        print("Supplier:", movement["supplier_id"] or "N/A")
        print("Location:", movement["location_id"])
        print("Date:", movement["timestamp"])


def search_movement():
    movements = load_data(MOVEMENT_FILE)

    movement_id = input("Movement ID: ").strip()

    movement = find_by_id(
        movements,
        movement_id
    )

    if not movement:
        print("Movement not found.")
        return

    for key, value in movement.items():
        print(f"{key}: {value}")
