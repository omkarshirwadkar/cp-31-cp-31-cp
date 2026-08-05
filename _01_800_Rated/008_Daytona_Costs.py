t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(c) for c in input().split()]
    if k in a:
        print("YES")
    else:
        print("NO")