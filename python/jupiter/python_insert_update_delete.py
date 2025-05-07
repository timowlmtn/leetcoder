def longest_increasing_contiguous_subarray_with_trace(arr):
    """
    Returns the longest strictly increasing contiguous subarray of arr,
    with print statements tracing the sliding-window logic.
    """
    n = len(arr)
    if n == 0:
        print("Input array is empty.")
        return []

    # Best window seen so far: [best_start, best_end)
    best_start, best_end = 0, 1
    # Current sliding window: [window_start, window_end)
    window_start, window_end = 0, 1

    print(
        f"Start: best=({best_start},{best_end}), window=({window_start},{window_end})"
    )
    print("-" * 50)

    # Sweep window_end across the array
    while window_end < n:
        print(
            f"Comparing arr[{window_end-1}]={arr[window_end-1]} → arr[{window_end}]={arr[window_end]}"
        )
        if arr[window_end] > arr[window_end - 1]:
            # Still increasing: expand window
            window_end += 1
            print(f"  Increasing → expand window to ({window_start},{window_end})")
        else:
            # Break in increase: check and reset
            print("  Break detected")
            current_len = window_end - window_start
            best_len = best_end - best_start
            if current_len > best_len:
                best_start, best_end = window_start, window_end
                print(
                    f"  New best window=({best_start},{best_end}), length={best_end-best_start}"
                )
            # Reset window to start at the break point
            window_start = window_end
            window_end = window_start + 1
            print(f"  Reset window to ({window_start},{window_end})")
        print("-" * 50)

    # Final check in case the longest run goes to the end
    current_len = window_end - window_start
    best_len = best_end - best_start
    if current_len > best_len:
        best_start, best_end = window_start, window_end
        print(
            f"Final update best window=({best_start},{best_end}), length={best_end-best_start}"
        )

    result = arr[best_start:best_end]
    print(
        f"Result: longest increasing contiguous subarray = arr[{best_start}:{best_end}] → {result}"
    )
    return result


# Example usage
if __name__ == "__main__":
    sample = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Input:", sample)
    longest_increasing_contiguous_subarray_with_trace(sample)
