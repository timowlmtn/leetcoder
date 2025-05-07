def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]


def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]


def reverse_string_2(s: str) -> str:
    """
    Reverse a string using recursion.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_2(s[:-1])


def reverse_string_3(s: str) -> str:
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return "".join(result)


if __name__ == "__main__":
    # Example usage
    input_string = "hello"
    # reversed_string = reverse_string(input_string)
    # print(f"Original string: {input_string}")
    # print(f"Reversed string: {reversed_string}")
    #
    # reversed_string = reverse_string_2(input_string)
    # print(f"Original string: {input_string}")
    # print(f"Reversed string: {reversed_string}")

    reversed_string = reverse_string_3(input_string)
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reversed_string}")
