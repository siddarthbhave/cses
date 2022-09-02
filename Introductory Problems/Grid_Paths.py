ref = input()

ans = 0
# seen = {(0,0)}
def dfs(x,y,steps, seen):
    global ans
    if x<0 or x>=7 or y<0 or y>=7 or steps > 49: return

    if x == 6 and y == 0:
        if steps == 48:
            ans += 1
        print(steps)
        return

    if ref[steps] == '?':
        for i,j in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx,ny = i+x, j+y
            if 0<=nx<7 and 0<=ny<7 and (nx,ny) not in seen:
                seen.add((nx,ny))
                dfs(nx,ny,steps+1, seen)

    elif ref[steps] == 'R':
        if 0 <= x < 7 and 0 <= y < 7 and (x, y+1) not in seen:
            seen.add((x,y+1))
            dfs(x, y+1, steps+1, seen)
    elif ref[steps] == 'L':
        if 0 <= x < 7 and 0 <= y < 7 and (x, y-1) not in seen:
            seen.add((x, y-1))
            dfs(x, y-1, steps+1, seen)
    elif ref[steps] == 'U':
        if 0 <= x < 7 and 0 <= y < 7 and (x-1, y) not in seen:
            seen.add((x-1,y))
            dfs(x-1, y, steps+1, seen)
    elif ref[steps] == 'D':
        if 0 <= x < 7 and 0 <= y < 7 and (x+1, y) not in seen:
            seen.add((x+1,y))
            dfs(x+1, y, steps+1, seen)

dfs(0,0,0, {(0,0)})
print(ans)
