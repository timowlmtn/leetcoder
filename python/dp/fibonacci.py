def fibonacci(n):
    def fibonacci_recursive(n):
        print(f"\t{n}")
        if n > 0:
            n = n + fibonacci_recursive(n - 1)
            return n
        else:
            return 0

    return fibonacci_recursive(n)


def main():
    print(f"Result: {fibonacci(3)}")


if __name__ == "__main__":
    main()
