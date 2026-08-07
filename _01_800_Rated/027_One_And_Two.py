t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    countK = a.count(2)
    if countK % 2:
        print(-1)
    else:
        currK = 0
        for i in range(n):
            if a[i] == 2:
                currK += 1
            if currK * 2 == countK:
                print(i + 1)
                break