# You have to start from 0 to X and come back to 0 and you have n fuel station in between
# No petrol pumps at 0 and X
# What is the minimum starting fuel the vehicle should have to complete the whole journey

t = int(input())
for _ in range(t):
    n, x = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    curr = 0
    ans = 0
    for i in a:
        ans = max(ans, i - curr)
        curr = i
    ans = max(ans, 2 * (x - a[-1]))
    print(ans)