def merge_two_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merge two sorted lists into a single sorted list.

    Args:
    list1 (list[int]): The first sorted list.
    list2 (list[int]): The second sorted list.

    Returns:
    list[int]: A new sorted list containing all elements from both input lists.
    """
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append any remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


if __name__ == "__main__":
    # Example usage
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_two_sorted_lists(list1, list2)
    print(f"Merged sorted list: {merged}")  # Output: [1, 2, 3, 4, 5, 6]

    list1 = [1, 3, 5, 7, 8]
    list2 = [2, 3, 4, 6, 7]
    merged = merge_two_sorted_lists(list1, list2)
    print(f"Merged sorted list: {merged}")  # Output: [1, 2, 3, 3, 4, 5, 6, 7, 7, 8]
