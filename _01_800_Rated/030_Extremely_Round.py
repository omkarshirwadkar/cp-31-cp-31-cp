t = int(input())
for _ in range(t):
    nArray = list(str(int(input())))
    ans = int(nArray[0]) + 9 * (len(nArray) - 1)
    print(ans)