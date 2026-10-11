
# Warehouse Management System

A Python-based warehouse management application for tracking
products, suppliers, storage locations, stock movements,
and inventory valuation.

## Features

- Product registration and search
- Product information updates
- Supplier management
- Warehouse location management
- Product-to-location assignment
- Product-to-supplier assignment
- Incoming stock transactions
- Outgoing stock transactions
- Stock movement history
- Negative stock prevention
- Low-stock reports
- Inventory valuation
- Location-wise inventory reports
- JSON data persistence

## Technologies Used

- Python
- JSON
- Datetime
- UUID
- OS

## Project Structure

```text
warehouse-management-system/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── product_manager.py
├── supplier_manager.py
├── location_manager.py
├── stock_manager.py
├── movement_manager.py
├── report_manager.py
├── data/
│   ├── products.json
│   ├── suppliers.json
│   ├── locations.json
│   └── movements.json
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/warehouse-management-system.git
```

Open the project directory:

```bash
cd warehouse-management-system
```

Run the application:

```bash
python main.py
```

No external packages are required.

## How to Use

1. Add a product and assign a unique SKU.
2. Register a supplier.
3. Create a warehouse storage location.
4. Assign the product to a location.
5. Assign a supplier if required.
6. Record incoming stock.
7. Record outgoing stock.
8. Review stock movement history.
9. Generate inventory and low-stock reports.

## Example

Product: Keyboard

SKU: KB-001

Unit Cost: ₹500

Stock Received: 20 units

Stock Issued: 5 units

Remaining Stock: 15 units

Inventory Value: ₹7,500

## Inventory Valuation

Inventory Value = Current Quantity × Unit Cost

## Future Improvements

- MySQL database
- Django web interface
- Role-based login
- Barcode scanning
- Purchase order management
- Stock transfer between locations
- PDF inventory reports
- Excel export
- Supplier purchase history
- Automated low-stock notifications

## Author

Kunal Karbhari

GitHub: https://github.com/developerKunal18

## Challenge

365 Days of Python Projects

Day 353 Completed
