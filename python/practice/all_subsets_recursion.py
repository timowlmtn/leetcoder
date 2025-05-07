def get_all_subsets(nums):
    """
    Generate all possible subsets of a given list of numbers using recursion.

    :param nums: List[int] - List of integers to generate subsets from.
    :return: List[List[int]] - List of all possible subsets.
    """
    result = []

    def backtrack(index, path):
        # When we've considered all elements, record the current subset
        if index == len(nums):
            result.append(path.copy())
            return

        # 1) Exclude nums[index]
        backtrack(index + 1, path)

        # 2) Include nums[index]
        path.append(nums[index])
        backtrack(index + 1, path)

        # backtrack, remove the last element
        path.pop()

    # start recursion with an empty path at index 0
    backtrack(0, [])
    return result


if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3]
    subsets = get_all_subsets(nums)
    print("All possible subsets:")
    for subset in subsets:
        print(subset)
