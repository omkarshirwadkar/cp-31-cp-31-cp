t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    for i in range(n - 1):
        if a[i] == 1:
            a[i] += 1
        if a[i + 1] == 1:
            a[i + 1] += 1
        if a[i + 1] % a[i] == 0:
            a[i + 1] += 1
    print(*a)