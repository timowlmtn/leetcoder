def valid_path_between_graphs(
    n: int, edges: list[list[int]], start: int, end: int
) -> bool:
    """
    Given an undirected graph represented as a list of edges and two nodes, determine if there is a valid path between the two nodes.
    """
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False


if __name__ == "__main__":
    # Example usage
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    start = 0
    end = 4
    print(valid_path_between_graphs(n, edges, start, end))  # Output: True

    start = 0
    end = 5
    print(valid_path_between_graphs(n, edges, start, end))  # Output: False

    n = 6
    edges = [[0, 1], [1, 2], [2, 3], [6, 7], [7, 8]]
    start = 0
    end = 3
    print(valid_path_between_graphs(n, edges, start, end))  # Output: True
