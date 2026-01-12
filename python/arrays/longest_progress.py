def get_longest_subseq(arr, k):
    if not arr:
        return 0

    S = set(arr)
    best = 0

    for x in S:
        if (x - k) not in S:
            # print(f"{x}")
            length = 1
            y = x + k
            while y in S:
                length += 1
                y += k

            best = max(best, length)

    return best

arr = list(map(int, input().split()))
k = int(input())

print(get_longest_subseq(arr, k))