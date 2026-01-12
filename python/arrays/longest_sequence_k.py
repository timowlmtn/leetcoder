def get_longest_subseq(arr, k):
    if not arr:
        return 0

    best = 1
    cur = 1

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == k:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
        # print(f"{i} {arr[i] - arr[i-1]} {cur} {best}")

    return best

arr = list(map(int, input().split()))
k = int(input())

print(get_longest_subseq(arr, k))