t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if a != sorted(a):
        print(0)
    else:
        minAns = 10 ** 9
        for i in range(n - 1):
            minAns = min(minAns, ((a[i + 1] - a[i]) // 2) + 1)
        print(minAns)