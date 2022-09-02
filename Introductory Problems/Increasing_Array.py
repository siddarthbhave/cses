n = int(input())
arr = list(map(int, input().split()))

prev = arr[0]
ans = 0
for i in range(1,n):
    if arr[i] < prev:
        ans += prev-arr[i]
    else:
        prev = arr[i]

print(ans)