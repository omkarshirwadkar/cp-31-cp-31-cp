t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]

    # CASE 1: Current Maximum between first and last
    ans = a[n - 1] - a[0]

    # Case 2: Difference between 1st and any number
    for i in range(1, n):
        ans = max(ans, a[i] - a[0])

    # Case 3: Difference between last and any number
    for i in range(n - 1):
        ans = max(ans, a[n - 1] - a[i])

    # Case 4: Maximum consecutive difference
    for i in range(n - 1):
        ans = max(ans, a[i] - a[i + 1])

    print(ans)