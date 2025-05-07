def find_target_sorted_array(sorted_arry):
    """
    Find the target in a sorted array using binary search.

    Args:
    sorted_arry (list[int]): The sorted array to search in.
    target (int): The target value to find.

    Returns:
    int: The index of the target in the sorted array, or -1 if not found.
    """
    left, right = 0, len(sorted_arry) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if sorted_arry[mid] == target:
            return mid
        elif sorted_arry[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # Example usage
    sorted_arry = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    index = find_target_sorted_array(sorted_arry)
    print(
        f"Index of {target} in the sorted array: {index}"
    )  # Output: Index of 5 in the sorted array: 4
