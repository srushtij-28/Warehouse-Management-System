import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PRODUCT_FILE = os.path.join(DATA_DIR, "products.json")
SUPPLIER_FILE = os.path.join(DATA_DIR, "suppliers.json")
LOCATION_FILE = os.path.join(DATA_DIR, "locations.json")
MOVEMENT_FILE = os.path.join(DATA_DIR, "movements.json")

MOVEMENT_TYPES = ["IN", "OUT"]
LOW_STOCK_DEFAULT = 5
