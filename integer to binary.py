n=int(input())
if n == 0:
    print(0)
binary = ''
while n:
    binary=str(n&1)+binary
    n>>=1
print(binary)
