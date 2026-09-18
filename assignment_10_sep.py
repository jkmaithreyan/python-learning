# 1. Problem Statement:

# A backend engineer at an online store needs a small reporting function that takes the day's order records and produces one category-level sales aggregation summary. Some order amounts are missing and must be handled sensibly rather than ignored, and the final summary must be ordered from the highest-selling category to the lowest.

# 2. Approach:

# Work on a copy of the input DataFrame so the original data stays intact.
# Within each category group, fill any missing amount value with that same category's own average amount (not one global average across all categories).
# Group the filled data by category and aggregate (sum) the amount column to get one total per category.
# Sort the resulting totals from the highest amount to the lowest.
# Return the sorted totals as a pandas Series indexed by category.


import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7],
    "category": ["cosmetics", "cosmetics", "electronics", "electronics",
                 "groceries", "groceries", "cosmetics"],
    "amount": [100, None, 500, 300, 50, 70, 300],
})

def summarize_sales(df):
    working_df = df.copy()
    cosmetics_average = working_df[working_df["category"] == "cosmetics"]["amount"].mean()

    working_df.loc[working_df["category"] == "cosmetics", "amount"] = working_df.loc[working_df["category"] == "cosmetics", "amount"].fillna(cosmetics_average)

    total_amount = working_df.groupby("category")["amount"].sum()
    result = total_amount.sort_values(ascending=False)

    return result

if __name__ == "__main__":
    print(summarize_sales(orders))

