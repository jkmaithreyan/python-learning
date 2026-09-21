# 1. Problem Statement:

# Your task: Write a Python function that computes funnel conversion rates and finds the bigger drop-off stage.

# You are a senior data analyst at a food delivery company. The product team tracks daily app opens, cart adds, and checkouts to spot where customers abandon the ordering process. Use the six days of activity data below to find the weaker funnel stage.

# 2. Approach:

# Load the sample data into a pandas DataFrame using the columns shown below.
# Sum the app_opens, add_to_cart, and checkouts columns across all rows.
# Compute the add-to-cart rate as add_to_cart sum divided by app_opens sum, times 100.
# Compute the checkout rate as checkouts sum divided by add_to_cart sum, times 100.
# Compare the two rates to work out which stage has the bigger percentage drop-off.
# Return a dictionary with both rates rounded to two decimals and the bigger-drop-off stage name.

import pandas as pd

data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    "app_opens": [500, 480, 510, 460, 530, 600],
    "add_to_cart": [220, 200, 230, 190, 250, 300],
    "checkouts": [95, 90, 100, 80, 110, 140],
}
df = pd.DataFrame(data)

def funnel_summary(df):

    app_opens_sum = df["app_opens"].sum()
    add_to_cart_sum = df["add_to_cart"].sum()
    checkouts_sum = df["checkouts"].sum()

    add_to_cart_rate = float(round(add_to_cart_sum / app_opens_sum * 100, 2))
    checkouts_rate = float(round(checkouts_sum / add_to_cart_sum * 100, 2))

    app_to_cart_dropoff = 100 - add_to_cart_rate
    cart_to_checkout_dropoff = 100 - checkouts_rate
    
    if app_to_cart_dropoff > cart_to_checkout_dropoff:
        biggest_drop_off_stage = "App_to_cart"
    else:
        biggest_drop_off_stage = "Cart_to_checkout"

    return {
        "Add_to_cart_rate" : add_to_cart_rate,
        "Checkouts_rate" : checkouts_rate,
        "Biggest_drop_off_stage" : biggest_drop_off_stage
    }


if __name__ == "__main__":
    print(funnel_summary(df))
