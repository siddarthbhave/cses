def solve(a,b):

    if ((2*a - b>=0) and (2*a - b ) % 3 == 0) and ((2*b - a) >= 0 and (2*b - a) % 3 == 0): return True
    else:
        return False

n = int(input())

for _ in range(n):
    x,y = list(map(int, input().split()))
    if solve(x,y):
        print('YES')
    else:
        print('NO')
