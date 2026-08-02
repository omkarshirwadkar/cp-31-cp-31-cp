# Can you sort an array by reversing a subarray of size not more than k, any number of times
# Print YES if possible else NO

t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if a == sorted(a):
        print("YES")
    else:
        if k == 1:
            print("NO")
        else:
            print("YES")