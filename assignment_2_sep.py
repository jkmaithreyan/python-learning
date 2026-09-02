# 1. Problem Statement:

# A sports analytics associate needs a quick Python summary script for two raw inputs collected before a match: a list of players' recent net-run scores, and a dictionary of squad details. The script must reshape the score list into a grid for pairwise comparison, and separately look up one player's row from a squad table built with pandas. Build a single script that produces both the reshaped score grid and the requested squad lookup.

# 2. Approach:

# Create a NumPy array from the given list of match scores.
# Reshape that array into 2 rows and 4 columns.
# Build a pandas DataFrame from the given squad dictionary.
# Use loc to retrieve the row for the requested player index.
# Determine the dtype of the DataFrame's "player" column.
# Print the reshaped array, the retrieved row, and the column dtype.
# 3. Expected Output:

# Sample input:

# SCORES = [45, 60, 12, 89, 34, 77, 5, 99]
# SQUAD = {"player": ["Rohit", "Kohli", "Bumrah"], "role": ["Batter", "Batter", "Bowler"]}
# ROW_INDEX = 1
# Expected output for that input:

# Reshaped scores:
# [[45 60 12 89]
#  [34 77  5 99]]

# Row at index 1 :
# player     Kohli
# role      Batter
# Name: 1, dtype: str

# Column dtype for "player": str


import numpy as np
import pandas as pd

SCORES = [45, 60, 12, 89, 34, 77, 5, 99]
SQUAD = {"player": ["Rohit", "Kohli", "Bumrah"], "role": ["Batter", "Batter", "Bowler"]}
ROW_INDEX = 1

def build_score_grid(scores):
    # TODO: create a NumPy array from `scores` and reshape it into 2 rows x 4 columns

    scores_array = np.array(scores)
    reshaped_scores_array = scores_array.reshape(2, 4)
    sorted_score = np.sort(scores_array)[::-1]

    return reshaped_scores_array, sorted_score

def build_squad_lookup(squad, row_index):
    # TODO: build a DataFrame from `squad`, fetch the row at `row_index` using loc,
    # and also return the dtype of the "player" column

    df = pd.DataFrame(squad)
    row = df.loc[row_index]
    data_type = df["player"].dtype

    return row, data_type

if __name__ == "__main__":
    grid, sorted_score = build_score_grid(SCORES)
    print("Reshaped scores:")
    print(grid)
    print("\nScores in descending order:")
    print(sorted_score)

    row, player_dtype = build_squad_lookup(SQUAD, ROW_INDEX)
    print("\nRow at index", ROW_INDEX, ":")
    print(row)
    print('\nColumn dtype for "player":', player_dtype)
