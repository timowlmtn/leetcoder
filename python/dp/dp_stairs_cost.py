def get_max_total_cost(n, steps, costs):
    print(f"{n} {steps} {costs}")

    NEG_INF = float("-inf")
    dp = [NEG_INF] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == NEG_INF:
            continue

        for step in steps:
            current = i + step
            if current <= n:
                dp[current] = max(dp[current], dp[i] + costs[current])
                print(f"{current} {i} {dp}")

    return None if dp[n] == NEG_INF else dp[n]

n = int(input())
steps = list(map(int, input().split()))
costs = list(map(int, input().split()))

print(get_max_total_cost(n, steps, costs))