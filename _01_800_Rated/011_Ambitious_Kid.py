n = int(input())
a = [int(x) for x in input().split()]
mini = 1000000
for i in a:
    if abs(i) < mini:
        mini = abs(i)
print(mini)