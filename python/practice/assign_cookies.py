def assign_cookies(greed: list[int], size: list[int]) -> int:
    """
    :param greed: List of greed factors of children
    :param size: List of sizes of cookies
    :return: Maximum number of children that can be content with the cookies
    """
    greed.sort()
    size.sort()

    child_i = 0
    cookie_i = 0

    while child_i < len(greed) and cookie_i < len(size):
        if greed[child_i] <= size[cookie_i]:
            child_i += 1
        cookie_i += 1

    return child_i


if __name__ == "__main__":
    # Example usage
    greed = [1, 2, 3]
    size = [1, 1]
    print(assign_cookies(greed, size))  # Output: 1

    greed = [1, 2]
    size = [1, 2, 3]
    print(assign_cookies(greed, size))  # Output: 2
