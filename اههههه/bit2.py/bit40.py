def count_ways(coins, n, index):
# If the amount reaches zero, there is only one way
    if n == 0:
        return 1
# If the amount is negative or the coins run out, there is no way
    if n < 0 or index == len(coins):
        return 0
# Two ways: Either use the current currency or bypass it.
    return count_ways(coins, n - coins[index], index) + count_ways(coins, n, index + 1)

# Available currency values
coins = [500, 100, 10, 5, 1]

# The amount required to be entered by the user
n = int(input("Enter the amount: "))

print("Number of ways:", count_ways(coins, n, 0))