def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    island_count = 0
    in_an_island = {}

    def depth_search(row_idx, col_idx):
        in_an_island[(row_idx, col_idx)] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            d_row, d_col = row_idx + direction[0], col_idx + direction[1]
            # If we fall within the grid
            if 0 <= d_row < rows and 0 <= d_col < cols and grid[d_row][d_col] == "1":
                in_an_island[(d_row, d_col)] = True

    for row in range(rows):
        for col in range(cols):
            # Check to see if we are on an island
            if grid[row][col] == "1":
                island_count = island_count + 1
                depth_search(row, col)

    print(island_count)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]


def main():
    print(f"Path: {count_islands(grid)}")


if __name__ == "__main__":
    main()
