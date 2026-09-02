# 1. Problem Statement:

# A backend engineer at a restaurant ordering platform needs a small file handling script so that today's discount does not have to be hard-coded into the ordering application every time it changes. Build a function save_discounted_orders(orders, discount_percent, filename) that takes a list of order dictionaries, applies a discount using NumPy, and saves the discounted orders as JSON lines in a log file so other services can read the updated prices later.

# 2. Approach:

# Pull the "price" value out of every order dictionary into a plain Python list.
# Convert that list of prices into a NumPy array using np.array().
# Apply the discount by multiplying the array elementwise by (1 - discount_percent / 100).
# Build a new list of order dictionaries where each order's "price" is replaced by its corresponding discounted value, keeping the other fields (order_id, item) unchanged.
# Open filename in write mode using a with block, and write each updated order dictionary as one JSON line with json.dumps(), followed by a newline character.
# Return the list of updated order dictionaries so the caller can also use them directly in Python.


import json
import numpy as np

def save_discounted_orders(orders, discount_percent, filename):
    prices = [order["price"] for order in orders]
    prices_array = np.array(prices)

    # Apply the discount
    discounted_prices = prices_array * (1 - discount_percent / 100)

    updated_orders = []

    # Build updated orders
    for i in range(len(orders)):
        updated_order = {
            "order_id": orders[i]["order_id"],
            "item": orders[i]["item"],
            "price": discounted_prices[i].item()
        }
        updated_orders.append(updated_order)

    with open(filename, "w") as f:
        # Write each order as one JSON line
        for order in updated_orders:
            f.write(json.dumps(order) + "\n")

    return updated_orders


if __name__ == "__main__":
    orders = [
        {"order_id": "O1", "item": "Dosa", "price": 100},
        {"order_id": "O2", "item": "Idly", "price": 60},
        {"order_id": "O3", "item": "Biryani", "price": 300},
    ]

    result = save_discounted_orders(orders, 10, "discounted_orders.txt")
    print(result)
    