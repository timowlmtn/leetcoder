def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 3:
        return 2

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


n = int(input())

print(fibonacci(n))