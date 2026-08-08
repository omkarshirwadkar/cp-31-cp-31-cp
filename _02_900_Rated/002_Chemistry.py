t = int(input())
for _ in range(t):
    n, k = [int(c) for c in input().split()]
    s = input()
    charArray = [0] * 26
    for ch in s:
        charArray[ord(ch) - ord('a')] += 1
    oddLength = 0
    for chCount in charArray:
        if chCount % 2:
            oddLength += 1
    if oddLength > k + 1:
        print("NO")
    else:
        print("YES")