t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    totalSum = sum(a)
    if totalSum & 1:
        print("NO")
    else:
        print("YES")