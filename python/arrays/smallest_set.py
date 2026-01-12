def smallest_missing_positive(nums):
    num_set = set(nums)
    x = 1

    while x in num_set:
        x += 1

    return x



n = int(input())

orderNumbers = []
for i in range(n):
    orderNumbers.append(int(input()))

print (smallest_missing_positive(orderNumbers))