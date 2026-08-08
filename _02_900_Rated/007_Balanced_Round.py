t = int(input())
for _ in range(t):
    n, k = [int(pf) for pf in input().split()]
    a = [int(pf) for pf in input().split()]
    seq = 1
    longSeq = 1
    a.sort()
    for i in range(n - 1):
        if a[i + 1] - a[i] <= k:
            seq += 1
        else:
            seq = 1
        longSeq = max(longSeq, seq)
    print(n - longSeq)