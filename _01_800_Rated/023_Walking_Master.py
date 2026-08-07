t = int(input())
for _ in range(t):
    a, b, c, d = [int(pj) for pj in input().split()]
    if d < b:
        print(-1)
    else:
        a = a + d - b
        if c > a:
            print(-1)
        else:
            print((d - b) + (a - c))