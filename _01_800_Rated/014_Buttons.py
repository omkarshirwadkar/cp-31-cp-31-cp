t = int(input())
for _ in range(t):
    a, b, c = [int(x) for x in input().split()]
    b += c // 2
    a += (c - (c // 2))
    if a > b:
        print("First")
    else:
        print("Second")