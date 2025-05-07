def get_all_subsets(nums):
    """
    Generate all possible subsets of a given list of numbers.

    :param nums: List[int] - List of integers to generate subsets from.
    :return: List[List[int]] - List of all possible subsets.
    """
    result = []
    n = len(nums)

    # Iterate through all possible combinations (2^n)
    for i in range(1 << n):
        subset = []
        for j in range(n):
            # Check if the j-th bit is set in i
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)

    return result


if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3]
    subsets = get_all_subsets(nums)
    print("All possible subsets:")
    for subset in subsets:
        print(subset)
