t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    maxZeros = 0
    currZeros = 0
    for ele in a:
        if not ele:
            currZeros += 1
        else:
            currZeros = 0
        maxZeros = max(maxZeros, currZeros)
    print(maxZeros)