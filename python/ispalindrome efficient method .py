def ispalindrome (s):
    l=0
    h=int(len(s)/2)
    for i in range(l,h):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True
a=input()
k=ispalindrome(a)
if k:
    print(1)
else:
    print(0)
