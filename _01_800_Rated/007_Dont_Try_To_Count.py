t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = input()
    b = input()
    ansFound = False
    for i in range(6):
        if b in a:
            ansFound = True
            break
        a = a + a
    if ansFound:
        print(i)
    else:
        print(-1)