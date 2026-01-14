def window_sum_zero(arr, k):
    if k <= 0 or k > len(arr):
        return []

    # print(arr)
    window_sum = sum(arr[:k])
    # print(f"init: {window_sum}")

    res = []

    if window_sum == 0:
        res.append(arr[:k])

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        print(f"{window_sum}")
        if window_sum == 0:
            res.append(arr[i - k + 1 : i + 1])
            print(f"{arr[i]} {arr[i - k]} {window_sum} {res}")

    return res

arr = list(map(int, input().split()))
k = int(input())
result = window_sum_zero(arr, k)
print('\n'.join([' '.join(map(str, x)) for x in result]))