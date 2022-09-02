def rec(n):
    if n == 1:
        return ['0', '1']
    

    tmp = rec(n-1)
    ans = []

    for i in tmp:
        ans.append('0'+i)
    
    for i in tmp[::-1]:
        ans.append('1'+i)

    return ans

n = int(input())

for i in rec(n):
    print(i)