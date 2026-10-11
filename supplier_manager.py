from config import SUPPLIER_FILE
from storage import load_data, save_data
from utils import generate_id, read_nonempty, find_by_id


def add_supplier():
    suppliers = load_data(SUPPLIER_FILE)

    name = read_nonempty("Supplier Name: ")
    phone = read_nonempty("Phone Number: ")
    address = read_nonempty("Address: ")

    if name is None or phone is None or address is None:
        return

    if not phone.isdigit() or not 10 <= len(phone) <= 15:
        print("Enter a valid phone number containing 10–15 digits.")
        return

    supplier = {
        "id": generate_id("SUP"),
        "name": name,
        "phone": phone,
        "address": address,
        "active": True
    }

    suppliers.append(supplier)
    save_data(SUPPLIER_FILE, suppliers)

    print("Supplier added successfully!")
    print("Supplier ID:", supplier["id"])


def view_suppliers():
    suppliers = load_data(SUPPLIER_FILE)

    if not suppliers:
        print("No suppliers found.")
        return

    for supplier in suppliers:
        print("-" * 40)
        print("ID:", supplier["id"])
        print("Name:", supplier["name"])
        print("Phone:", supplier["phone"])
        print("Address:", supplier["address"])
        print("Active:", supplier["active"])


def search_supplier():
    suppliers = load_data(SUPPLIER_FILE)

    supplier_id = input("Supplier ID: ").strip()
    supplier = find_by_id(suppliers, supplier_id)

    if supplier:
        for key, value in supplier.items():
            print(f"{key}: {value}")
    else:
        print("Supplier not found.")
