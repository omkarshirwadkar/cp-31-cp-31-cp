from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    counterA = Counter(a)
    if len(counterA) == 1:
        print("Yes")
    elif len(counterA) == 2:
        if abs(list(counterA.values())[0] - list(counterA.values())[1]) <= 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")