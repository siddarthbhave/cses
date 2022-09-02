from collections import Counter
s = input()
c = Counter(s)

end = ''
ans1,ans2 = '',''
for ch, freq in c.items():
    if freq%2:
        if end != '':
            print('NO SOLUTION')
            exit()
        end = ch*freq
    else:
        ans1 += ch*(freq//2)
        ans2 += ch*(freq//2)

print(ans1+end+ans2[::-1])