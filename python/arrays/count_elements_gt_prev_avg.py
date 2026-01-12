def gt_prev_avg(elements):
    print(f"{elements}")
    count = 0
    current_sum = elements[0]

    for i in range(1, len(elements)):

        avg = current_sum / i

        if elements[i] > avg:
            count += 1
            print(f"i={i}, val={elements[i]}, avg={avg}")

        current_sum = current_sum + elements[i]

    return count


elements = list(map(int, input().split()))

print(gt_prev_avg(elements))