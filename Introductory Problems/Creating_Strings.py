s = input()
ans = set()

def recurse(mask, cur):
    if len(cur) == len(s):
        ans.add(cur)
        return

    for i in range(len(mask)):
        if not mask[i]:
            mask[i] = True
            recurse(mask, cur+s[i])
            mask[i] = False


recurse([False]*len(s),'')
print(len(ans))
for i in sorted(ans):
    print(i)