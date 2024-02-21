num = list(map(int,input().split()))
total = 0
for i in range(len(num)):
    
    if num[i] == 0 and i > 2:
        if total == 0:
            total += num[i-1]
            total += num[i-2]
            total += num[i-3]
    

print(total)