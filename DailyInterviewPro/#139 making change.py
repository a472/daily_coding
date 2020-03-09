"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of possible coins in cents, and an amount (in cents) n,
return the minimum number of coins needed to create the amount n.
If it is not possible to create the amount using the given coin denomination, return None.
"""


def make_change(coins, n):

    dp = [float('inf')]*(n+1)
    dp[0]=0
    for val in range(n+1):
        for coin in coins:
            if val>=coin:
                dp[val]=min(dp[val],1+dp[val-coin])
    if dp[n]==float('inf'):
        return None
    return dp[n]


print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
