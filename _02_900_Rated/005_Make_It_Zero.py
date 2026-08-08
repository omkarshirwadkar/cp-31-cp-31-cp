t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pf) for pf in input().split()]
    if not n % 2:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(1, 2)
        print(1, 2)
        print(2, n)
        print(2, n)