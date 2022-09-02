def solve(x,y):
    num = 0
    if x>y:
        if x%2:
            num = (x-1)**2 + 1
            num = num+y-1
        else:
            num = (x)**2 
            num = num-y+1
    else:
        if y%2:
            num = (y)**2
            num = num-x+1
        else:
            num = (y-1)**2 + 1
            num = num+x-1

    print(num)
    return

n = int(input())
for _ in range(n):
    x,y = list(map(int, input().split()))
    solve(x,y)