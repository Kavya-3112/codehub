def isPalindrome(self, x):
    temp=x
    rem=0
    while x>0:
        r=x%10
        rem=10*rem+r
        x//=10
    if temp==rem:
        return True 
    else:
        return False
