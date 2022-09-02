n = int(input())

if (n*(n+1))//2 % 2: print('NO')
else:
    print('YES')
    target = (n*(n+1))//4
    l1,l2 = [],[]
    sum1,sum2 = 0,0

    for i in range(n,0,-1):
        if sum1 <= sum2:
            sum1 += i
            l1.append(i)
        else:
            sum2 += i
            l2.append(i)

    print(len(l1))
    for i in l1:
        print(i, end=' ')
    print()
    print(len(l2))
    for i in l2:
        print(i, end=' ')