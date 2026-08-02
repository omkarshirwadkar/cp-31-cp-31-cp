# Players can add or subtract 1 to the number it their turn
# Player 1 plays first and want the number to be divisible by 3
# Player 2 wants to stop player 1 from winning for 10 moves
# Print who wins after playing their move

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 3:
        print("First")
    else:
        print("Second")