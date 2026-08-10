t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    longestRepeatingString = 1
    currRepeatingString = 1
    currString = s[0]
    for i in range(1, n):
        if s[i] == currString:
            currRepeatingString += 1
            longestRepeatingString = max(longestRepeatingString, currRepeatingString)
        else:
            currString = s[i]
            currRepeatingString = 1
    print(longestRepeatingString + 1)