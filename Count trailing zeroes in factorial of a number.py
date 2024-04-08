n = int(input())
ans= 0
t=5
while t<=n:
    ans+=n//t
    t*=5
print("Count of trailing 0s in 100! is",ans)
