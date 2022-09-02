s = input()

prev = None
count = 1
ans = 0
for i in s:
    if i == prev:
        count += 1
    else:
        ans = max(ans, count)
        count = 1

    prev = i

ans = max(ans, count)
print(ans)