ORDERS = [
    {"order_id": 101, "item": "Laptop", "amount": 55000},
    {"order_id": 102, "item": "Mouse", "amount": 800},
    {"order_id": 103, "item": "Keyboard", "amount": 1500},
    {"order_id": 104, "item": "Monitor", "amount": 55000},
    {"order_id": 105, "item": "Webcam", "amount": 2200},
    {"order_id": 106, "item": "Speaker", "amount": 3200},
]

def second_highest_amount(orders):

    amounts = []
    
    for order in orders:
        amounts.append(order["amount"])

    highest_amount = amounts[0]
    second_highest = 0

    for amount in amounts:
        if amount > highest_amount:
            highest_amount = amount

    for amount in amounts:
        if amount < highest_amount and amount > second_highest:
            second_highest = amount

    return second_highest

if __name__ == "__main__":
    print(second_highest_amount(ORDERS))
