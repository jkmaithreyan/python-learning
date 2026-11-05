import pandas as pd
sales = pd.DataFrame({"store": ["N", "S", "N", "E", "S", "N", "E"], "product": ["tea", "tea", "cake", "tea", "pie", "cake", "tea"], "units": [10, None, 4, 7, 5, 4, 7]})

# Print the shape of sales and the number of missing values in units in one print call.
# Remove the repeated rows (keeping the first occurrence) into clean and print its shape.
# Fill the missing units in clean with the mean of the available units and print that mean together with the filled value at row label 1 in one print call.
# Group clean by store, sum units, and print the totals of stores N, S and E in one print call.
# Sort the store totals in descending order and print the top store and its total in one print call. Then print how many rows of clean are for tea using value_counts().
# Explain why the repeated rows are removed before the mean is computed, why the missing value is filled rather than dropped, and what the row count would have been if duplicates had been checked only on the store column.

# Expected Output
# (7, 3) 1
# (5, 3)
# 6.5 6.5
# 14.0 11.5 7.0
# N 14.0
# 3


#step 1
clean = sales.drop_duplicates()

#step 2
avg_units = clean["units"].mean()
clean.fillna(avg_units)

#step 3
store_total_sales = clean.groupby("store")["units"].sum()
order = store_total_sales["units"]
print(order)

print(sales.shape, sales["units"].isnull().sum())

print(clean.shape)

print(avg_units, clean["units"][1])

print()




# Q: 15
# Problem Statement
# A multiplex sells tickets by age group. You will write a pricing function with a default parameter, process a queue of visitors with skipping and early stopping, tally the age categories in a dictionary and explain the scope and loop-control rules involved.

# Dataset
# ages = [5, 17, 0, 34, 68, 12, 45]
# An age of 0 is an invalid entry.

# Tasks
# Write ticket_price(age, base=250) using an if-elif-else chain with return statements: visitors below 12 pay half of base, visitors aged 60 or above pay 60 percent of base, and everyone else pays base. Print ticket_price(5), ticket_price(34), ticket_price(68) and ticket_price(34, 300) in one print call.
# Loop over ages. Skip invalid ages (zero or below) with continue. For each valid visitor add the ticket price to total and increase count. Stop the loop with break as soon as, after adding, total is at least 700. Print Tickets: <count> Revenue: <total>.
# In the same loop keep a dictionary tally that counts the tickets sold per category: "child" (below 12), "adult" and "senior" (60 or above). Update it before the break check, and print tally after the loop.
# Explain briefly: (a) why the order of the branches in Task 1 gives each visitor exactly one price, (b) which value of base is used by ticket_price(34) and why, (c) what happens if you print base after the function call and why, and (d) why the revenue is 775.0 and not 700 or 625, and which ages are never processed.
# Expected Output
# 125.0 250 150.0 300
# Tickets: 4 Revenue: 775.0
# {'child': 1, 'adult': 2, 'senior': 1}
# Submission Format
# Paste your complete code and its printed output, then your written answers for Task 4, all in the input box.

# Note: You may use any IDE (online: Google Colab, Jupyter Notebook; offline: VS Code, PyCharm, or similar) to write, run, and test your code. You must disable all AI-based extensions (GitHub Copilot, Tabnine, Codeium, etc.) before starting. AI tools of any kind are not permitted and will lead to disqualification. Submit your complete code as a copy-pasted snippet in the input box — do not submit a URL, notebook link, GitHub repository, or Google Drive file.