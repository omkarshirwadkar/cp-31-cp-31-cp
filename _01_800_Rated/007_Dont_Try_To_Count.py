t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = input()
    b = input()
    i = 0
    ansFound = False
    while i <= 7:
        if b in a:
            ansFound = True
            break
        a = a + a
        i += 1
    if ansFound:
        print(i)
    else:
        print(-1)