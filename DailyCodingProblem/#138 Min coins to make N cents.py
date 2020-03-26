"""
This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""
def get_min_coins(change,coins):
    dp = [float('inf')]*(change+1)
    dp[0]=0

    for val in range(1,change+1):
        for coin in coins:
                if val>=coin:
                    dp[val]=min(dp[val],1+dp[val-coin])
    if dp[change]==float('inf'):
        return -1
    return dp[change]


change = 3
coins = [1,2]

print(get_min_coins(change, coins))

