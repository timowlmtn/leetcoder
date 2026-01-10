def max_mod(lists, M):
    dp = {0}

    for arr in lists:
        new_dp = set()
        for previous_sum in dp:
            for num in arr:
                candidate = (previous_sum + num) % M
                print(f"previous_sum: {previous_sum}, candidate: {candidate}")
                new_dp.add(candidate)
        dp = new_dp

    return max(dp)


if __name__ == "__main__":
    K, M = map(int, input().split())

    lists = []
    for _ in range(K):
        parts = list(map(int, input().split()))
        # If the line is "Ni a1 a2 ...", use: lists.append(parts[1:])
        # If the line is just "a1 a2 ...", use:
        lists.append(parts)

    print(max_mod(lists, M))
