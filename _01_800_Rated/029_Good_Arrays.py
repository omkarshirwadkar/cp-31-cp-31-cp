t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    ans = 0
    currParity = a[0] % 2
    grp = 1
    for i in range(1, n):
        parity = a[i] % 2
        if parity == currParity:
            grp += 1
        else:
            ans += grp - 1
            grp = 1
            currParity = parity
    ans += grp - 1
    print(ans)