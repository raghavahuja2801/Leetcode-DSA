def is_safe(maze, x, y, N):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1

def solve_maze(maze, x, y, N, solution):
    if x == N - 1 and y == N - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, N):
        solution[x][y] = 1
        if solve_maze(maze, x + 1, y, N, solution):
            return True
        if solve_maze(maze, x, y + 1, N, solution):
            return True
        solution[x][y] = 0
        return False

    return False

def rat_in_maze(maze, N):
    solution = [[0] * N for _ in range(N)]
    if not solve_maze(maze, 0, 0, N, solution):
        return "No path exists"
    return solution

# Example usage
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
N = 4
result = rat_in_maze(maze, N)
if result != "No path exists":
    for row in result:
        print(row)
else:
    print(result)
