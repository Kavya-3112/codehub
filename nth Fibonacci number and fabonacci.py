a=int(input())
lis=[0,1]
for i in range(0,a):
    lis.append(lis[-1]+lis[-2])
print(lis[a])
/********************************/
a=int(input())
lis=[0,1]
for i in range(0,a):
    lis.append(lis[-1]+lis[-2])
print(lis)
