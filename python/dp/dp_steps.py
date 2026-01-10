def climb(n_steps):
    print(n_steps)
    if n_steps <= 2:
        return n_steps
    first, second = 1, 2

    print(first, second)

    for i in range(3, n_steps + 1):
        third = first + second
        print(third)
        print(first, second)
        first, second = second, third
        print(second, third)

    return second


def main():
    print(f"Result: {climb(4)}")


if __name__ == "__main__":
    main()
