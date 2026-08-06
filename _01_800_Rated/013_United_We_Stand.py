t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[0] == a[-1]:
        print(-1)
    else:
        firstCount = a.count(a[0])
        print(firstCount, n - firstCount)
        print(*a[:firstCount])
        print(*a[firstCount:])