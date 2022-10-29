def walk_through_maze(x, y, maze):
    maze[y][x] = -1

    if (x != 4) or (y != 4):
        if y > 0 and maze[y - 1][x] == 0:
            walk_through_maze(x, y - 1, maze)

        if y < 4 and maze[y + 1][x] == 0:
            walk_through_maze(x, y + 1, maze)

        if x > 0 and maze[y][x - 1] == 0:
            walk_through_maze(x - 1, y, maze)

        if x < 4 and maze[y][x + 1] == 0:
            walk_through_maze(x + 1, y, maze)


n_tests = int(input())

for i in range(n_tests):
    maze, x, y = [], 0, 0

    while len(maze) < 5:
        line = list(map(int, input().split()))
        if line:
            maze.append(line)

    walk_through_maze(0, 0, maze)
    print('COPS') if maze[4][4] == -1 else print ('ROBBERS')