import random

width = 60
height = 30
snake_char = "@"
fence_char = "*"
snake_x = random.randint(1, width-2)
snake_y = random.randint(1, height-2)
board = [[" " for _ in range(width)] for _ in range(height)]


for i in range(height):
    board[i][0] = fence_char
    board[i][width-1] = fence_char

for j in range(width):
    board[0][j] = fence_char
    board[height-1][j] = fence_char


board[snake_y][snake_x] = snake_char


def draw_board():
    for row in board:
        print("".join(row))



print("Hova?")
draw_board()

while True:
    move = input().lower()

    if move == "balra":
        snake_x -= 1
    elif move == "jobbra":
        snake_x += 1
    elif move == "fel":
        snake_y -= 1
    elif move == "le":
        snake_y += 1
    elif move == "meguntam":
        break
    if (
        snake_x == 0 or
        snake_x == width - 1 or
        snake_y == 0 or
        snake_y == height - 1
    ):
        break
    board[snake_y][snake_x] = snake_char
    draw_board()
print("Most ennyi volt, szép napot!")