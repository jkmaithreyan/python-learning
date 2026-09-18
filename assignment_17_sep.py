# 1. Problem Statement:

# Your task: Write a Python script that groups sales by branch and plots a labeled bar chart comparing total branch sales.

# You are a senior data analyst at a retail chain with three branches. Your manager wants one chart that instantly shows which branch is ahead, without a spoken explanation alongside it.

# 2. Approach:

# Load the sales data into a pandas DataFrame from the inlined CSV sample below.
# Group the DataFrame by branch and sum the sales column to get one total per branch.
# Convert the grouped result back into a plain DataFrame so branch and sales are separate columns.
# Plot a Matplotlib bar chart using the branch names on the x-axis and total sales on the y-axis.
# Add a title, an x-axis label, and a y-axis label that names the unit being measured (dollars).
# Rotate the x-axis branch labels and apply a layout adjustment so no labels overlap.


import pandas as pd
import matplotlib.pyplot as plt
import io
import seaborn as sns
import plotly.express as px

# Sample input is already provided as a CSV string below.
csv_data = """branch,week,sales
Bangalore,1,15000
Bangalore,2,16200
Bangalore,3,15800
Chennai,1,18000
Chennai,2,17500
Chennai,3,19000
Pune,1,12000
Pune,2,12500
Pune,3,13100
"""

df = pd.read_csv(io.StringIO(csv_data))

def total_sales_by_branch(df):

    branch_totals = df.groupby("branch")["sales"].sum().reset_index()
    return branch_totals

def plot_branch_sales(branch_totals):

    #bar chart using matplotlib
    plt.bar(branch_totals["branch"], branch_totals["sales"])

    plt.title("Total sales in each branch")
    plt.xlabel("Branch")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()

    #bar chart using ploty
    fig = px.bar(
        branch_totals,
        x="branch",
        y="sales",
        title="Total sales in each branch",
        labels={
            "branch": "Barnch",
            "sales" : "sales",
        }
    )
    fig.show()

    #line chart using seaborn
    sns.lineplot(data = df, x = "week", y = "sales", hue = "branch")

    plt.title("weekly sales analysis")
    plt.xlabel("weeks")
    plt.ylabel("sales ($)")
    plt.tight_layout()
    plt.show()

    #line chart using plotly
    fig = px.line(
        df,
        x="week",
        y="sales",
        color="branch",
        title="sales by week",
        labels={
            "week" : "Week",
            "sales" : "sales",
            "branch": "Barnch"
        }
    )

    fig.show()

    
if __name__ == "__main__":
    branch_totals = total_sales_by_branch(df)
    print(branch_totals)
    plot_branch_sales(branch_totals)
