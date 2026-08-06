t = int(input())
for _ in range(t):
    n = int(input())
    b = [int(x) for x in input().split()]
    a = []
    a.append(b[0])
    for i in range(1, n):
        if b[i] < b[i - 1]:
            a.append(b[i])
        a.append(b[i])
    print(len(a))
    print(*a)