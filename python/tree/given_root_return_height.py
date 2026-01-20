def get_height(n, values, left_child, right_child):
    # print(f"{n} {values} {left_child} {right_child}")

    if n == 0:
        return -1

    root = 0

    # print(f"Starting DFS from root index {root} (value={values[root]})\n")

    def dfs(node, depth=0):
        indent = " " * depth
        if node == -1:
            # print(f"{indent}Reached null child → return -1")
            return -1

        # print(f"{indent}Visiting node index={node}, value={values[node]}")

        left_h = dfs(left_child[node], depth+1)
        right_h = dfs(right_child[node], depth+1)

        height = 1 + max(left_h, right_h)

        # print(
        #     f"{indent}Node {values[node]}: "
        #     f"left_height={left_h}, right_height={right_h} "
        #     f"→ height={height}\n"
        # )

        return height

    return dfs(root)

n = int(input())
values = list(map(int, input().split()))
left_child = list(map(int, input().split()))
right_child = list(map(int, input().split()))

print(get_height(n, values, left_child, right_child))