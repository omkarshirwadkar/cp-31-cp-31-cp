# You have to sort the permutation after a finite number of operation
# operation --> if ai-1 < ai and ai > ai+1 then swap ai and ai+1
# Solution --> we can never move the 0th index rest can moved to the desired position
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if a[0] == 1:
        print("YES")
    else:
        print("NO")