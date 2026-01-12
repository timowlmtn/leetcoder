
def make_change_ways(n, coins):
    print(f"{n} {coins}")

    dp = [0] * (n + 1)
    dp[0] = 1  # one way to make 0: use no coins

    for coin in coins:
        print(f"\nUsing coin {coin}")
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
            print(f"{coin} {amount}  amount={amount}: dp={dp}")

    return dp[n]


n = int(input())
coins = list(map(int, input().split()))

print(make_change_ways(n, coins))