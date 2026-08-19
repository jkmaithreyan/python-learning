# Problem Statement:

# A retail data analyst runs a quick spot-check on a short list of daily sales entries recorded during a shift. The analyst needs a script that logs the position of every entry in the list, computes the overall total of all entries, and separately computes the total contributed only by the even-valued entries — all using the accumulator and indexing patterns for loops in Python.

# Constraints & Requirements:

# Use a for loop combined with range() and len() to access each entry by its index position (do not use any library functions beyond built-ins).
# Use an accumulator variable, initialized to 0 before the loop, to build up the running total — the same pattern used for summing a list.
# Use the modulo operator (%) inside the loop to determine whether each entry is even, and accumulate a separate running total of just the even-valued entries.
# The function must return both totals as a tuple in the form (total_sum, even_sum).
# Inside the loop, print each entry alongside its index position in the format Position <index>: <value>.
# Inlined Sample Data & Inputs:

# Sample input (verbatim, shown to student):

# numbers = [1, 5, 4, 7, 9, 10, 55, 75, 33]
# Expected output for that sample:

# Position 0: 1
# Position 1: 5
# Position 2: 4
# Position 3: 7
# Position 4: 9
# Position 5: 10
# Position 6: 55
# Position 7: 75
# Position 8: 33
# Total: 199
# Even total: 14


def analyze_sales(numbers):
    total_sum = 0
    even_sum = 0
    for i in range(len(numbers)):
        # TODO: read the current entry using index-based access
        value = numbers[i]

        # TODO: print the entry with its position, in the required format
        print(f"Position {i}: {value}")

        # TODO: add the entry to total_sum using the accumulator pattern
        total_sum += value

        # TODO: check whether the entry is even using the modulo operator,
        #       and if so, add it to even_sum
        
        if value % 2 == 0:
            even_sum += value
    return total_sum, even_sum

if __name__ == "__main__":
    numbers = [1, 5, 4, 7, 9, 10, 55, 75, 33]
    total, evens = analyze_sales(numbers)
    print("Total:", total)
    print("Even total:", evens)
