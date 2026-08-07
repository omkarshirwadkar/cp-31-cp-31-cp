t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    sumArr = 0
    prodArr = 1
    for ele in a:
        sumArr += ele
        prodArr *= ele
    ans = 0
    while sumArr < 0 or prodArr != 1:
        sumArr += 2
        prodArr *= -1
        ans += 1
    print(ans)