CRATE_SIZE = 4
FREE_DELIVERY_THRESHOLD = 500

def process_orders(orders):
    results = []
    for order in orders:
        # TODO: cast unit_price to a float and quantity to an int
        unit_price = float(order["unit_price"])
        quantity = int(order["quantity"])

        # TODO: compute total_cost using the multiplication operator
        total_cost = unit_price * quantity

        # TODO: compute crates using floor division and leftover using modulus
        crates = quantity // CRATE_SIZE
        leftover = quantity % CRATE_SIZE

        # TODO: compute free_delivery using the >= comparison operator
        free_delivery = total_cost >= FREE_DELIVERY_THRESHOLD

        results.append({
            "order_id" : order["order_id"],
            "total_cost" : total_cost,
            "crates" : crates,
            "leftover" : leftover,
            "free_delivery" : free_delivery
        })
    return results

if __name__ == "__main__":
    sample_orders = [
        {"order_id": "1", "unit_price": "20", "quantity": "12"},
        {"order_id": "2", "unit_price": "50.45", "quantity": "3"},
        {"order_id": "3", "unit_price": "20", "quantity": "30"},
    ]
    print(process_orders(sample_orders))
