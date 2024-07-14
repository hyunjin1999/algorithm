n, m, x, y, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# top: dice[1][1], bottom: dice[3][1]
dice = [[0, 0, 0] for _ in range(4)]


def is_range(x, y) -> bool:
    return 0 <= x < n and 0 <= y < m


def print_top(x, y) -> None:

    # 이동한 칸에 쓰여 있는 수가 0인 경우
    if li[x][y] == 0:
        li[x][y] = dice[3][1]   # 칸에 쓰여 있는 수 변경
        print(dice[1][1])       # 주사위 top 출력

    # 이동한 칸에 쓰여 있는 수가 0이 아닌 경우
    elif li[x][y] != 0:
        dice[3][1] = li[x][y]   # 주사위 밑면 수 변경
        li[x][y] = 0            # 칸에 쓰여 있는 수 0으로 변경
        print(dice[1][1])       # 주사위 top 출력


for command in commands:

    # 동쪽방향일 때
    if command == 1 and is_range(x, y + 1):
        y += 1
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
        print_top(x, y)

    # 서쪽방향일 때
    elif command == 2 and is_range(x, y - 1):
        y -= 1
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
        print_top(x, y)

    # 북쪽방향일 때
    elif command == 3 and is_range(x - 1, y):
        x -= 1
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
        print_top(x, y)

    # 남쪽방향일 때
    elif command == 4 and is_range(x + 1, y):
        x += 1
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
        print_top(x, y)
