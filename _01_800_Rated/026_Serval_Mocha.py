import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    minGcd = max(a)
    for i in range(n):
        for j in range(i + 1, n):
            minGcd = min(minGcd, math.gcd(a[i], a[j]))
    if minGcd <= 2:
        print("Yes")
    else:
        print("No")