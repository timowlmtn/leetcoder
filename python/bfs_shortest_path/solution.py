from collections import deque

grid = [["S", 0, 1, 0, "E"], [0, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 1]]


def find_shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    visited = {}

    # Start out by appending the first
    for row_idx in range(rows):
        for col_idx in range(cols):
            if grid[row_idx][col_idx] == "S":
                queue.append((row_idx, col_idx, 0))
                visited[(row_idx, col_idx)] = True

    while queue:
        row_idx, col_idx, dist = queue.popleft()

        print(grid[row_idx][col_idx], dist)

        if grid[row_idx][col_idx] == "E":
            return dist

        for d_row, d_col in directions:
            row_n, col_n = row_idx + d_row, col_idx + d_col
            if (
                0 <= row_n < rows
                and 0 <= col_n < cols
                and (row_n, col_n) not in visited
            ):
                if grid[row_n][col_n] == 0 or grid[row_n][col_n] == "E":
                    if grid[row_n][col_n] == 0:
                        rooms = dist + 1
                    else:
                        rooms = dist

                    queue.append((row_n, col_n, rooms))
                    visited[(row_n, col_n)] = True

    return -1  # No path found


def main():
    print(f"Path: {find_shortest_path(grid)}")


if __name__ == "__main__":
    main()
