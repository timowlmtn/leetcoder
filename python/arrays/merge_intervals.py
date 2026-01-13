def merge_intervals(n, l, intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    # print(f"{n} {l} {intervals}")
    merge = list()
    merge.append(intervals[0][:])
    m_i = 0
    for i in range(1, len(intervals)):
        # print(f"{i} {merge} {intervals[i]}")
        if intervals[i][0] <= merge[m_i][l-1]:
            merge[m_i][l-1] = max(merge[m_i][l-1], intervals[i][l-1])
        else:
            merge.append(intervals[i])
            m_i += 1

    return merge


n = int(input())
l = int(input())

intervals = []
for i in range(0, n):
    intervals.append(list(map(int, input().split())))

print(merge_intervals(n, l, intervals))