t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    a.sort(reverse=True)
    if a[0] == a[-1]:
        print("NO")
    else:
        print("YES")
        b = []
        for i in range(n//2):
            b.append(a[i])
            b.append(a[n - i - 1])
        if n % 2:
            b.append(a[n//2])
        print(*b)