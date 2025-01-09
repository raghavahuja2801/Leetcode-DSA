def exist(board, word):
    def backtrack(i, j, idx):
        if idx == len(word):
            return True
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != word[idx]:
            return False

        temp, board[i][j] = board[i][j], '#'
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if backtrack(i + dx, j + dy, idx + 1):
                return True
        board[i][j] = temp
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    return False

# Example usage
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"
print(exist(board, word))  # Output: True
