def allocateBandwidthMaxRevenue(n, sizes, revenues, B):
    items = []

    for i in range(n):
        s = sizes[i]
        r = revenues[i]

        if s == 0:
            density = 0
        else:
            density = r / s

        items.append((density, s, r))
        # print(f"{items}")
    items.sort(key=lambda x: x[0], reverse=True)

    total = 0.0
    remaining = B

    for density, s, r in items:
        if remaining <= 0:
            break

        take = min(s, remaining)
        total += density * take
        # print(f"{take} {total} {s} {remaining}")
        remaining -= take

    return total


N = int(input().strip())

sizes_count = int(input().strip())

sizes = []

for _ in range(sizes_count):
    sizes_item = int(input().strip())
    sizes.append(sizes_item)

revenues_count = int(input().strip())

revenues = []

for _ in range(revenues_count):
    revenues_item = int(input().strip())
    revenues.append(revenues_item)

B = int(input().strip())

result = allocateBandwidthMaxRevenue(N, sizes, revenues, B)

print(result)

