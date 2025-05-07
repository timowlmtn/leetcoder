def valid_parenthesis(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    # Example usage
    s = "{[]}"
    print(valid_parenthesis(s))  # Output: True

    s = "([)]"
    print(valid_parenthesis(s))  # Output: False

    s = "{[()]}"
    print(valid_parenthesis(s))  # Output: True
