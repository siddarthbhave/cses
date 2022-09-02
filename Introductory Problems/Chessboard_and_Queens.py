board = []
for _ in range(8):
    board.append(list(input()))

ans = 0
row, col, diag, anti = set(), set(), set(), set()

def backtrack(cur):
    global ans

    if cur == 8:
        ans += 1
        if ans%300 == 0:
            for i in board: print(i)
            print()
        return

    for c in range(8):
        if board[cur][c] == '.' and c not in col and cur not in row and cur+c not in diag and c-cur not in anti:
            board[cur][c] = 'Q'
            row.add(cur)
            col.add(c)
            diag.add(cur+c)
            anti.add(c-cur)
            backtrack(cur+1)
            board[cur][c] = '.'
            row.remove(cur)
            col.remove(c)
            diag.remove(cur+c)
            anti.remove(c-cur)

backtrack(0)
print(ans)