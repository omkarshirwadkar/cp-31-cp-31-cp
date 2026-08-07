t = int(input())
for _ in range(t):
    n, a, b = [int(pj) for pj in input().split()]
    case1 = n > a + b + 1
    case2 = n == a == b
    if case1 or case2:
        print("Yes")
    else:
        print("No")