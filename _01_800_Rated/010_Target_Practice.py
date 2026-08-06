t = int(input())
target = [
    "1111111111",
    "1222222221",
    "1233333321",
    "1234444321",
    "1234554321",
    "1234554321",
    "1234444321",
    "1233333321",
    "1222222221",
    "1111111111"
]
for _ in range(t):
    ans = 0
    for i in range(10):
        a = input()
        for j in range(10):
            if a[j] == "X":
                ans += int(target[i][j])
    print(ans)