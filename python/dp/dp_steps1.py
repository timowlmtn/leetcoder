def get_steps(n, steps):
    print(f"{n} {steps}")
    dp = (n+1) * [0]
    dp[0] = 1
    for i in range(0, n):
        for step in steps:
            next_step = i+step
            if next_step <= n:
                dp[next_step] += dp[i]
                print(f"{i} {next_step} {dp}")
    return dp[n]

n = int(input())

steps = list(map(int, input().split()))

print(get_steps(n, steps))