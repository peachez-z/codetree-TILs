txt = list(map(str, input().split()))
ans = []
for i in range(len(txt)):
    if i == 1 or i == 4 or i == 7 :
        ans.append(txt[i])
print(*ans)