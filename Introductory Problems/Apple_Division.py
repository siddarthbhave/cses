n = int(input())
arr = list(map(int, input().split()))
ans = float('inf')

def backtrack(idx, sum1, sum2):
    global ans
    if idx == len(arr):
        ans = min(ans, abs(sum1-sum2))
        return ans

    backtrack(idx+1, sum1+arr[idx], sum2)
    backtrack(idx+1, sum1, sum2+arr[idx])

backtrack(0,0,0)
print(ans)