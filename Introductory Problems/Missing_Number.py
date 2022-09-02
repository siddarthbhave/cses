n = int(input())
arr = list(map(int, input().split()))

_sum = sum(arr)

print(((n*(n+1))//2) - _sum)