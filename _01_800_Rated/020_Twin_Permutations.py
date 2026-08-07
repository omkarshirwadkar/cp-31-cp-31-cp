t = int(input())
for _ in range(t):
    n = int(input())
    b = [n - int(pj) + 1 for pj in input().split()]
    print(*b)