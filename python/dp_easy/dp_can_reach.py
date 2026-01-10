def reachable_after_k_steps(k):
    positions = {0}  # before any steps

    for step in range(1, k + 1):
        new_positions = set()

        for pos in positions:
            new_positions.add(pos + 1)
            new_positions.add(pos + 2)

        print(f"After {step} step(s): {new_positions}")
        positions = new_positions

    return positions



if __name__ == "__main__":
    k = int(input())
    print(reachable_after_k_steps(k))