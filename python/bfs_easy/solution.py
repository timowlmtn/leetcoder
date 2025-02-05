from collections import deque

grid = [[0, 1, 0], [0, 0, 1]]


def get_nearest_1(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    visited = {}

    for row_idx in range(rows):
        for col_idx in range(cols):
            if grid[row_idx][col_idx] == 0:
                queue.append((row_idx, col_idx, 0))
                visited[(row_idx, col_idx)] = True
                break
        if queue:
            break

    # print(f"Found starter row {queue}")

    while queue:
        row_idx, col_idx, dist = queue.popleft()

        for d_row, d_col in directions:
            new_row, new_col = row_idx + d_row, col_idx + d_col
            if rows > new_row >= 0 == grid[new_row][new_col] and 0 <= new_col < cols:
                grid[row_idx][col_idx] = dist + 1
                queue.append((new_row, new_col, dist + 1))

    return grid


def main():
    print(f"Original grid: {grid}")
    print(f"Updated grid: {get_nearest_1(grid)}")


if __name__ == "__main__":
    main()
