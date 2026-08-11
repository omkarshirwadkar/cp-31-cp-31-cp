t = int(input())
for _ in range(t):
    n, q = [int(pj) for pj in input().split()]
    a = [int(pj) for pj in input().split()]
    prefSumA = [0]
    for i in range(n):
        prefSumA.append(prefSumA[i] + a[i])
    for i in range(q):
        l, r, k = [int(pj) for pj in input().split()]
        currSum = prefSumA[r] - prefSumA[l - 1]
        modifiedSum = k * (r - l + 1)
        if ((abs(modifiedSum - currSum) + prefSumA[-1]) % 2):
            print("YES")
        else:
            print("NO")

            