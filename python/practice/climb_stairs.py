def climb_stairs(n: int) -> int:
    """
    Given an integer n, return the number of distinct ways to climb to the top.
    You can either climb 1 or 2 steps at a time.
    """
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second


if __name__ == "__main__":
    # Example usage
    n = 5
    print(f"Number of distinct ways to climb {n} steps: {climb_stairs(n)}")  # Output: 8
