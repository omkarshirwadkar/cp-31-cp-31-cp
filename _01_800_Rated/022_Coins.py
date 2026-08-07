t = int(input())
for _ in range(t):
    n, k = [int(pj) for pj in input().split()]
    case1 = (n % 2 == 1 and k % 2 == 0)
    if case1:
        print("NO")
    else:
        print("YES")