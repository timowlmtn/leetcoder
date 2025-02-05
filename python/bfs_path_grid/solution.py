from collections import deque

grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]


def find_dist_bottom_right(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = {}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Append the top right to the deque
    queue.append((0, 0, 0))

    # Prevent loops
    visited[(0, 0)] = True

    while queue:
        row, col, dist = queue.popleft()

        if (row, col) == (rows - 1, cols - 1):
            return dist + 1

        for d_row, d_con in directions:
            row_n, col_n = row + d_row, col + d_con
            if (
                0 <= row_n < rows
                and 0 <= col_n < cols
                and grid[row_n][col_n] == 0
                and (row_n, col_n) not in visited
            ):
                visited[(row_n, col_n)] = True
                queue.append((row_n, col_n, dist + 1))

    # no path found
    return -1


def main():

    print(f"Original grid: {grid}")

    moves = find_dist_bottom_right(grid)

    print(f"Shortest moves: {moves}")


if __name__ == "__main__":
    main()
