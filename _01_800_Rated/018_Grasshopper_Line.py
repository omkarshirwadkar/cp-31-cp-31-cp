t = int(input())
for _ in range(t):
    x, k = [int(pj) for pj in input().split()]
    if not x % k:
        print(2)
        print(x - 1, 1)
    else:
        print(1)
        print(x)