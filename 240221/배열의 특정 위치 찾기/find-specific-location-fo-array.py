num = list(map(int,input().split()))
two = 0 
three = 0
nthree = 0
for i in range(1, 10+1):
    if i % 2 == 0:
        two += num[i-1]
    elif i % 3 == 0 :
        nthree +=1
        three += num[i-1]
print(two, three/nthree)