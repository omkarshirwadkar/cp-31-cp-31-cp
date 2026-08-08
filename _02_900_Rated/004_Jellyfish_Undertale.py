t = int(input())
for _ in range(t):
    a, b, n = [int(pf) for pf in input().split()]
    x = [int(pf) for pf in input().split()]
    ans = b
    for ele in x:
        ans += min(ele, a - 1)
    print(ans)