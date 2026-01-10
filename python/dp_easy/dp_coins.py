def coins_match(coins, amount):
    INF = 10
    dp = [INF] * (T + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        print(f"--- {a}")
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
                print(f"a: {a}, c: {c} dp[a]: {dp[a]}")

    return -1 if dp[amount] == INF else dp[amount]

if __name__ == "__main__":
    T = int(input())
    coins = list(map(int, input().split()))

    print(f"T={T} coins={coins}")

    print(coins_match(coins, T))