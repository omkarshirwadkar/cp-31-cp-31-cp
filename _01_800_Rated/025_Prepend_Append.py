t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    ans = n
    for i in range(n // 2):
        if s[i] == s[n - 1 - i]:
            break
        ans -= 2
    print(ans)