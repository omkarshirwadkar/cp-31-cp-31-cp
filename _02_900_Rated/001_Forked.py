t = int(input())
for _ in range(t):
    # Taking Input
    a, b = [int(x) for x in input().split()]
    xk, yk = [int(x) for x in input().split()]
    xq, yq = [int(x) for x in input().split()]

    # The directions to move for the knight
    dx, dy = [-1, -1, 1, 1], [-1, 1, -1, 1]

    # Set to store positions of knight
    kingMoves = set()
    queenMoves = set()

    # Move in all 4 directions with 2 options a,b
    # In total 8 moves for both king and queen
    for i in range(4):
        kingMoves.add((xk + dx[i] * a, yk + dy[i] * b))
        kingMoves.add((xk + dx[i] * b, yk + dy[i] * a))

        queenMoves.add((xq + dx[i] * a, yq + dy[i] * b))
        queenMoves.add((xq + dx[i] * b, yq + dy[i] * a))

    # Calculate overlapping moves
    ans = 0
    for i in kingMoves:
        if i in queenMoves:
            ans += 1
    print(ans)