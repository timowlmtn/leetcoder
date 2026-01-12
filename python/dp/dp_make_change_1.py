def make_change(n, coins):
    print(f"{n} {coins}")
    dp = [0] * (n+1)
    dp[0] = 1

    for amount in range(1, n+1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] += dp[amount - coin]
            print(f"{coin} {amount} {dp}")

    return dp[n]

n = int(input())
coins = list(map(int, input().split()))

print(make_change(n, coins))