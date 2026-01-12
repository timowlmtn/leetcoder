def smallest_missing_positive(nums):
    # print(f"{nums}")

    n = len(nums)
    i = 0

    # print(nums)
    while i < n:
        v = nums[i]
        correct_idx = v - 1
        # print(f"   {v} {nums[correct_idx]}")
        if 1 <= v <= n and nums[correct_idx] != v:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            # print(f"*{i} {v} {correct_idx}")
        else:
            i += 1
            # print(f"{i} {v} {correct_idx}")

    # print(nums)
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n+1


n = int(input())

orderNumbers = []
for i in range(n):
    orderNumbers.append(int(input()))

print (smallest_missing_positive(orderNumbers))