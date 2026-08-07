t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    xorA = 0
    for ele in a:
        xorA ^= ele
    if n % 2 == 0 and xorA:
        print(-1)
    else:
        print(xorA)