t = int(input())
for _ in range(t):
    n, k, x = [int(pj) for pj in input().split()]
    case1 = (k == 1 and k == x)
    case2 = (k == 2 and x == 1 and n % 2 == 1)
    if case1 or case2:
        print("NO")
    else:
        print("YES")
        if x != 1:
            print(n)
            print(*[1 for i in range(n)])
        else:
            if n % 2 == 0:
                print(n // 2)
                print(*[2 for j in range(n // 2)])
            else:
                m = n - 3
                print(m // 2 + 1)
                print(*[2 if j > 0 else 3 for j in range(m // 2 + 1)])