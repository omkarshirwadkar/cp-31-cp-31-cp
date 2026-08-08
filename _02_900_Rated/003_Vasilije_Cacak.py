# Is it possible to choose k distinct integers between 1 and n whose sum is x

t = int(input())
for _ in range(t):
    n, k, x = [int(pj) for pj in input().split()]
    if x < k:
        print("NO")
    else:
        sumOfFirstKElements = ((k + 1) * k) // 2
        sumOfLastKElements = ((n - k + 1 + n) * k) // 2
        if sumOfFirstKElements <= x <= sumOfLastKElements:
            print("YES")
        else:
            print("NO")