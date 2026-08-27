# 1. Problem Statement:

# A backend engineer is auditing a batch of order-total amounts pulled from a payment gateway log. Some entries are negative refund adjustments or zero placeholders and must be ignored. Among the remaining positive totals, the engineer needs to find the very first one whose digits read the same forwards and backwards — without converting any number to a string. Build a Python function that scans the totals in their given order and returns the first such positive, digit-palindromic total, stopping the scan as soon as it is found.

# 2. Approach:

# Iterate through the totals in the order given.
# For each total that is zero or negative, skip it and move on to the next total without processing it further.
# For each remaining (positive) total, reverse its digits using the digit-by-digit technique: repeatedly extract the last digit with % 10, build up the reversed value with reverse * 10 + digit, and remove the last digit with // 10 until nothing is left.
# Compare the reversed value to the original total; if they are equal, stop scanning immediately and return that total.
# If no positive total in the whole list matches its own reversal, return None.
# 3. Expected Output:

# Sample input:

# ORDER_TOTALS = [45, -12, 121, 88, 0, 1331, 12345678, 500]
# Expected output for that input:

# 121

ORDER_TOTALS = [45, -12, 121, 88, 0, 1331, 12345678, 500]

def first_palindrome_total(totals):

    for total in totals:

        if total <= 0:
            continue

        reverse = 0
        original_total = total

        while total > 0:
            digit = total % 10
            reverse = reverse * 10 + digit
            total = total // 10

        if original_total == reverse:
            return reverse

    return None

if __name__ == "__main__":
    print(first_palindrome_total(ORDER_TOTALS))

