num = list(map(int, input().split()))
a = 0
b = 0
ans = 0
for i in range(10):
    if i % 2 == 0:
        a += num[i]
    else:
        b += num[i]

if a >= b : 
    ans = a - b
else:
    ans = b - a

print(ans)