def two_numbers_match(numbers, target):
    idx_start = 0
    idx_end = len(numbers) - 1

    while idx_start < idx_end:
        current_sum = numbers[idx_start] + numbers[idx_end]
        if current_sum == target:
            return idx_start
        elif current_sum < target:
            idx_start = idx_start + 1
        else:
            idx_end = idx_end - 1


print(two_numbers_match([1, 2, 3, 10], 5))

print(two_numbers_match([1, 2, 3, 6, 8, 9, 10], 17))
