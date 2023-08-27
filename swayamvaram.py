
a=int(input())
bride=list(input())
groom=list(input())
for i in bride:
    if i in groom:
        groom.remove(i)

    else:
        break
print(len(groom))
