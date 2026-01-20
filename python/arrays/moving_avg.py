def moving_avg(n, vals, k):
    if k > n or k == 0:
        return 0

    avg = list()
    avg.append(sum(vals[0:k]) / k)
    # print(f"{vals} = {avg}")

    for i in range(k, n):
        cur_range = vals[i - k + 1:i + 1]
        avg.append(sum(cur_range) / k)
        # print(f"{i} {i - k} {vals[i-k+1:i+1]} {avg[i-k]} ** {cur_range} {avg}")

    return avg


n = int(input())
vals = list(map(int, input().split()))
k = int(input())
print(moving_avg(n, vals, k))