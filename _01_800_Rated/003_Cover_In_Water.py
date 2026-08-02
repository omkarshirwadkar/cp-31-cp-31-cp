# op1 = fill water into an empty cell
# op2 = move water from one cell to an empty cell
# if there's water in (i - 1) cell and (i + 1) cell then cell i is filled automatically
# what is the minimum number of op1 used to fill the whole row

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    thrice = "..."
    twice = ".."
    if thrice in s:
        print(2)
    else:
        print(s.count("."))
