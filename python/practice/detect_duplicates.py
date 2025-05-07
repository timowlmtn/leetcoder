from typing import List


def detect_duplicates(nums: List[int]) -> List[int]:
    """
    Detect duplicates in a list of integers and return the duplicates.

    :param nums: List of integers
    :return: List of duplicates
    """
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates) if duplicates else [-1]


if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3, 4, 5, 1, 2]
    print(detect_duplicates(nums))  # Output: [1, 2]

    nums = [1, 2, 3, 4, 5]
    print(detect_duplicates(nums))  # Output: [-1]
