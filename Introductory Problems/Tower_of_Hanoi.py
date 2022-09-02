# !!GOLD
n = int(input())

def find_mid(start, end):
    if start+end == 3: return 3
    if start+end == 4: return 2
    return 1


def recurse(disks, start, end):
    ans = []
    mid = find_mid(start, end)
    if disks == 2:
        ans.append((start, mid))
        ans.append((start, end))
        ans.append((mid, end))
        return ans
    else:
        l1 = recurse(disks-1, start, mid)
        l1.append((start, end))
        return l1+recurse(disks-1, mid, end)


if n==1:
    print(1)
    print(1,3)
else:
    ans = recurse(n,1,3)
    print(len(ans))
    for i,j in ans:
        print(i,j)