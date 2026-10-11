import uuid
from datetime import datetime


def generate_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_by_id(records, record_id, key="id"):
    return next(
        (
            record for record in records
            if record.get(key) == record_id
        ),
        None
    )


def read_nonempty(prompt):
    value = input(prompt).strip()

    if not value:
        print("This field is required.")
        return None

    return value


def read_positive_number(prompt, allow_zero=False):
    try:
        value = float(input(prompt))

        if value < 0 or (value == 0 and not allow_zero):
            print("Enter a valid positive number.")
            return None

        return value

    except ValueError:
        print("Enter a valid number.")
        return None


def money(amount):
    return f"₹{amount:.2f}"
